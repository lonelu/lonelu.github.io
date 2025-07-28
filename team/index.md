---
title: Team
nav:
  order: 1
  tooltip: About our team
---

{% include section.html %}

<!-- PI成员 -->
{% include list.html data="pi" component="portrait"  %}

# {% include icon.html icon="fa-solid fa-users" %}Team
团队成员

{% include section.html %}

<!-- 非PI成员：使用 invert 反转过滤 -->
{% include list.html data="members" component="portrait" filters="role: pi, invert: true" %}

{% include section.html background="images/background.jpg" dark=true %}
欢迎有志之士加入我们!

{% include section.html %}

{% capture content %}
{% endcapture %}

{% include grid.html style="square" content=content %}
