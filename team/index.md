---
title: Team
nav:
  order: 1
  tooltip: About our team
---

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)" %}

# {% include icon.html icon="fa-solid fa-users" %}Team

团队成员

{% include section.html %}

{% include list.html data="members" component="portrait"  %}


{% include section.html background="images/background.jpg" dark=true %}

欢迎有志之士加入我们!

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
