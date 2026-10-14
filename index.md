---
title: Home
footer-minimal: true
nav:
  order: 0
  tooltip: Home
---

<size>full</size>

<div class="home-hero">
  <div class="home-hero__copy">
    <div class="home-hero__wordmark">
      <h1>Lu Lab</h1>
      <p>Tsinghua Protein Design Center</p>
    </div>
  </div>

  {% include protein-hero.html %}
</div>

{% include section.html size="wide" %}

<div id="research-directions" class="home-directions" markdown="1">

## Research Directions

<p class="home-directions__intro">Three interconnected directions spanning molecular binding, catalysis, and proteomics.</p>

<div class="research-direction-grid">
  <article class="research-direction-card">
    <div class="research-direction-card__visual">
      <span class="research-direction-card__number" aria-hidden="true">01</span>
      <img src="{{ '/images/research-direction-1.png' | relative_url }}" alt="Overlay of a rucaparib-bound designed protein structure and its computational design model">
    </div>
    <div class="research-direction-card__content">
      <p class="research-direction-card__label">Molecular binding</p>
      <h3>De Novo Design of Molecular Binding Proteins</h3>
      <p>We design proteins that selectively recognize drugs, metals, glycans, proteins, and other molecular targets. By integrating structural database mining with emerging protein design technologies, we develop functional binders for biomedical research, diagnostics, and therapeutic applications.</p>
    </div>
  </article>

  <article class="research-direction-card">
    <div class="research-direction-card__visual">
      <span class="research-direction-card__number" aria-hidden="true">02</span>
      <img src="{{ '/images/research-direction-2.png' | relative_url }}" alt="Designed alpha-helical enzyme structure with a catalytic center">
    </div>
    <div class="research-direction-card__content">
      <p class="research-direction-card__label">Catalysis</p>
      <h3>Computational Design of De Novo Enzymes</h3>
      <p>We develop computational methods for designing enzymes that catalyze specific chemical reactions. Our research combines custom protein scaffold databases, deep learning, and computational chemistry to create artificial enzymes with practical scientific and biomedical value.</p>
    </div>
  </article>

  <article class="research-direction-card">
    <div class="research-direction-card__visual">
      <span class="research-direction-card__number" aria-hidden="true">03</span>
      <img src="{{ '/images/research-direction-3.png' | relative_url }}" alt="O-glycoproteomics workflow from protein and glycan databases to fragment indexing">
    </div>
    <div class="research-direction-card__content">
      <p class="research-direction-card__label">Proteomics</p>
      <h3>Protein Design–Enabled Proteomics</h3>
      <p>We develop new proteomics technologies and algorithms based on engineered proteins and enzymes, including limited-proteolysis proteomics and proximity-labeling proteomics. These approaches support drug screening and the discovery of disease mechanisms and therapeutic targets.</p>
    </div>
  </article>
</div>

</div>
