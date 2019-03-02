---
layout: default
---
Tags:
<div class="tags">
  {% assign sortedTags = site.tags | sort %}
  {% for tag in sortedTags %}
    <span class="tag">
      <a href="#{{ tag[0] }}">{{ tag[0] }}</a> ({{ tag[1].size }})
    </span>
  {% endfor %}
</div>

<div class="archive-post-list">

  {% for tag in sortedTags %}
    <h1><a name="{{ tag[0] }}"></a>{{ tag[0] }} ({{ tag[1].size }})</h1>
    <ul>
    {% for post in tag[1] %}
      <li><span>{{ post.date | date: "%B %-d, %Y" }}</span> - <a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
    </ul>
  {% endfor %}

</div>
