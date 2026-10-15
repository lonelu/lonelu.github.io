"""Add locally hosted Figure 1 images to generated publication citations.

The updater prefers PubMed Central because its article and figure pages expose a
stable, public image URL.  A failed lookup is deliberately non-fatal: the site
template renders its local fallback image until a later scheduled run succeeds.
"""

import json
import mimetypes
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, urljoin, urlparse
from urllib.request import Request, urlopen


USER_AGENT = "LuLab publication updater/1.0 (https://lonelu.github.io/)"
IMAGE_DIR = Path("images/publications")
IMAGE_ROUTE = "images/publications"
TIMEOUT = 30


class FigureImageParser(HTMLParser):
    """Extract the full-size image used by a PMC figure page."""

    def __init__(self):
        super().__init__()
        self.src = ""

    def handle_starttag(self, tag, attrs):
        if self.src or tag.lower() != "img":
            return
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if "graphic" in classes and attrs.get("src"):
            self.src = attrs["src"]


def _request(url):
    return Request(url, headers={"User-Agent": USER_AGENT})


def _doi(citation):
    identifier = str(citation.get("id", ""))
    if identifier.lower().startswith("doi:"):
        return identifier[4:].strip()
    return ""


def _filename(citation, doi, extension):
    year = str(citation.get("date", "publication"))[:4]
    slug = re.sub(r"[^a-z0-9]+", "-", doi.lower()).strip("-")
    return f"{year}-{slug}-fig1{extension}"


def _existing_image(citation, doi):
    """Return a previously downloaded deterministic image, if present."""
    year = str(citation.get("date", "publication"))[:4]
    slug = re.sub(r"[^a-z0-9]+", "-", doi.lower()).strip("-")
    matches = sorted(IMAGE_DIR.glob(f"{year}-{slug}-fig1.*"))
    return matches[0] if matches else None


def _resolve_pmcid(doi):
    endpoint = (
        "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
        f"?format=json&tool=lulab-site&email=webmaster%40lonelu.github.io&ids={quote(doi)}"
    )
    with urlopen(_request(endpoint), timeout=TIMEOUT) as response:
        records = json.load(response).get("records", [])
    return records[0].get("pmcid", "") if records else ""


def _figure_image_url(figure_url):
    with urlopen(_request(figure_url), timeout=TIMEOUT) as response:
        html = response.read().decode("utf-8", errors="replace")
    parser = FigureImageParser()
    parser.feed(html)
    return urljoin(figure_url, parser.src) if parser.src else ""


def _extension(image_url, content_type):
    suffix = Path(urlparse(image_url).path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".gif", ".webp"}:
        return ".jpg" if suffix == ".jpeg" else suffix
    guessed = mimetypes.guess_extension(content_type.split(";", 1)[0].strip())
    return ".jpg" if guessed == ".jpe" else (guessed or ".jpg")


def add_publication_images(citations, warn=print):
    """Mutate citations with local images; return the number downloaded."""
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    downloaded = 0

    for citation in citations:
        if citation.get("image"):
            continue

        doi = _doi(citation)
        if not doi:
            continue

        existing = _existing_image(citation, doi)
        if existing:
            citation["image"] = existing.as_posix()
            continue

        try:
            pmcid = _resolve_pmcid(doi)
            if not pmcid:
                continue

            figure_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/figure/F1/"
            image_url = _figure_image_url(figure_url)
            if not image_url:
                raise RuntimeError("PMC Figure 1 page did not contain an image")

            with urlopen(_request(image_url), timeout=TIMEOUT) as response:
                content_type = response.headers.get("Content-Type", "image/jpeg")
                image_data = response.read()

            if not content_type.lower().startswith("image/") or not image_data:
                raise RuntimeError(f"unexpected Figure 1 response: {content_type}")

            output = IMAGE_DIR / _filename(
                citation, doi, _extension(image_url, content_type)
            )
            output.write_bytes(image_data)
            citation["image"] = f"{IMAGE_ROUTE}/{output.name}"
            citation["figure"] = figure_url
            downloaded += 1
        except Exception as error:
            warn(f"Could not download Figure 1 for doi:{doi}: {error}")

    return downloaded
