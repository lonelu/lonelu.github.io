---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

### 欢迎联系！欢迎加入！..........................欢迎
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

{%
  include button.html
  type="email"
  text="lonelu@whu.edu.cn"
  link="lonelu@whu.edu.cn"
%}
{%
  include button.html
  type="phone"
  text="没有了"
  link="---"
%}
{%
  include button.html
  type="address"
  tooltip="Our location on Maps for easy navigation"
  link="https://www.sps.tsinghua.edu.cn/"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/photo.jpg"
  caption="不知道放啥照片"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/photo.jpg"
  caption="不知道放啥照片"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html dark=true %}

{% capture col1 %}
不知道写啥
{% endcapture %}

{% capture col2 %}
不知道写啥
{% endcapture %}

{% capture col3 %}
不知道写啥
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}
