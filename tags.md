---
layout: default
---
Tags:
<div class="tags">
  {% assign sortedTags = site.tags | sort %}
  {% for tag in sortedTags %}
    <a href="/tag/{{ tag[0] }}">{{ tag[0] }}</a> ({{ tag[1].size }})<br>
  {% endfor %}
</div>
