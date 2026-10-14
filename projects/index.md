---
title: Resources
nav:
  order: 2
  tooltip: Software and tools
---

# {% include icon.html icon="fa-solid fa-screwdriver-wrench" %}Resources

Research software and computational frameworks developed by Lu Lab for protein design, structural modeling, and molecular analysis.

{% include section.html %}

## Software

<div class="resource-list">
  {% for resource in site.data.projects %}
    <article class="resource-card">
      <div class="resource-card__visual{% if resource.image %} resource-card__visual--image{% endif %}" aria-hidden="true">
        {% if resource.image %}
          <img{% if resource.image_is_icon %} class="resource-card__image--icon"{% endif %} src="{{ resource.image | relative_url | uri_escape }}" alt="">
        {% else %}
          <span>{{ resource.mark }}</span>
        {% endif %}
      </div>

      <div class="resource-card__content">
        <h3>{{ resource.title }}</h3>
        <p>{{ resource.description }}</p>

        {% if resource.link %}
          <a class="resource-card__link" href="{{ resource.link | relative_url | uri_escape }}">
            View resource
            {% include icon.html icon="fa-solid fa-arrow-right" %}
          </a>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</div>
