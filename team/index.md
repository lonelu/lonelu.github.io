---
title: People
nav:
  order: 3
  tooltip: About our team
---

{% include section.html %}

# {% include icon.html icon="fa-solid fa-users" %}People

## PI

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}

## Manager

{% include list.html data="members" component="portrait" filter="role == 'manager'" %}

## Postdoc

{% include list.html data="members" component="portrait" filter="role == 'postdoc'" %}

## PhD

{% include list.html data="members" component="portrait" filter="role == 'phd'" %}

## Undergraduate

{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %}

{% include section.html %}

## Alumni

{% assign alumni = site.members | where: "role", "alumni" | sort: "name" %}
<div class="alumni-list">
  {% for member in alumni %}
    <span>{{ member.name }}</span>
  {% endfor %}
</div>
