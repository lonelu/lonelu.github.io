---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

<p class="contact-intro">
  We&rsquo;re hiring passionate postdocs, research assistants, and students&mdash;join us!
</p>

{%
  include button.html
  type="email"
  text="lei_lu@tsinghua.edu.cn"
  link="lei_lu@tsinghua.edu.cn"
%}

<div class="contact-details" aria-label="Lu Lab location details">
  <div class="contact-detail">
    <span class="contact-detail__icon" aria-hidden="true">
      {% include icon.html icon="fa-solid fa-building-columns" %}
    </span>
    <div>
      <strong>Address</strong>
      <span>Biomedical Building, Tsinghua University, Beijing</span>
    </div>
  </div>

  <div class="contact-detail">
    <span class="contact-detail__icon" aria-hidden="true">
      {% include icon.html icon="fa-solid fa-flask" %}
    </span>
    <div>
      <strong>Laboratory</strong>
      <span>Room C301</span>
    </div>
  </div>

  <div class="contact-detail">
    <span class="contact-detail__icon" aria-hidden="true">
      {% include icon.html icon="fa-solid fa-door-open" %}
    </span>
    <div>
      <strong>Office</strong>
      <span>Room C316</span>
    </div>
  </div>
</div>

## {% include icon.html icon="fa-solid fa-map-location-dot" %}Find Us

<div class="contact-map">
  <iframe
    title="Map showing the Biomedical Building at Tsinghua University"
    src="https://api.map.baidu.com/marker?location=40.0128,116.32705&amp;title=Lu%20Lab&amp;content=Biomedical%20Building%2C%20Tsinghua%20University%2C%20Beijing&amp;output=html"
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
  ></iframe>
</div>

<p class="contact-map-link">
  <a href="https://api.map.baidu.com/marker?location=40.0128,116.32705&amp;title=Lu%20Lab&amp;content=Biomedical%20Building%2C%20Tsinghua%20University%2C%20Beijing&amp;output=html">
    Open in Baidu Maps {% include icon.html icon="fa-solid fa-up-right-from-square" %}
  </a>
</p>

## Affiliations

<div class="affiliation-grid">
  <a
    class="affiliation-card affiliation-card--sps"
    href="https://www.sps.tsinghua.edu.cn/"
    target="_blank"
    rel="noopener noreferrer"
    aria-label="School of Pharmaceutical Sciences, Tsinghua University"
  >
    <img
      src="{{ 'images/affiliations/sps-logo.jpg' | relative_url }}"
      alt="School of Pharmaceutical Sciences, Tsinghua University"
      width="380"
      height="100"
      loading="lazy"
    >
  </a>

  <a
    class="affiliation-card"
    href="https://www.frcbs.tsinghua.edu.cn/"
    target="_blank"
    rel="noopener noreferrer"
    aria-label="Beijing Frontier Research Center for Biological Structure"
  >
    <img
      src="{{ 'images/affiliations/frcbs.svg' | relative_url }}"
      alt="Beijing Frontier Research Center for Biological Structure"
      width="812"
      height="99"
      loading="lazy"
    >
  </a>

  <a
    class="affiliation-card"
    href="https://cls.tsinghua.edu.cn/"
    target="_blank"
    rel="noopener noreferrer"
    aria-label="Tsinghua-Peking Center for Life Sciences"
  >
    <img
      src="{{ 'images/affiliations/cls.png' | relative_url }}"
      alt="Tsinghua-Peking Center for Life Sciences"
      width="223"
      height="81"
      loading="lazy"
    >
  </a>
</div>
