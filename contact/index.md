---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

### 欢迎联系！欢迎加入！


{%
  include button.html
  type="email"
  text="lei_lu@tsinghua.edu.cn"
  link="lei_lu@tsinghua.edu.cn"
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
  image="images/水木清华.jpg"
  caption="水木清华"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/荷塘月色.jpg"
  caption="荷塘月色"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html dark=true %}

{% capture col1 %}
天行健
{% endcapture %}

{% capture col2 %}
君子以自强不息
{% endcapture %}



{% include cols.html col1=col1 col2=col2  %}
