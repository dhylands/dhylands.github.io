---
layout: post
title: OX - More clamps and a TinyG firmware issue
date: '2015-04-26T12:39:00.000-07:00'
author: Dave Hylands
tags:
- OX
modified_time: '2015-04-26T12:41:10.932-07:00'
thumbnail: http://4.bp.blogspot.com/-hu2aWsSSwT4/VT0vbVQEvhI/AAAAAAAAhVw/NyDeV7mcza4/s72-c/IMG_20150424_183821.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-8406492533135605137
blogger_orig_url: http://blog.davehylands.com/2015/04/ox-more-clamps-and-tinyg-firmware-issue.html
---

I printed some clamps and knobs on my 3D printer:
[![]({{ site.url }}/images/2015-04-26/image-0000.jpg)]({{ site.url}}/images/2015-04-26/image-0000.jpg)

{% include ox-related.md %}

I put them together like this:

[![]({{ site.url }}/images/2015-04-26/image-0001.jpg)]({{ site.url}}/images/2015-04-26/image-0001.jpg)


You can find the stl files [here](https://github.com/dhylands/3D-Printed-
Parts/tree/master/OX/Low-Profile-Knob), and the original OnShape CAD files
[here](https://cad.onshape.com/documents/ac25f8aa27194f018107d8a3/w/d9c6e6dc98fe415180a348a6/e/273716e84f30487d979d0def).

I used a cut piece of 1/4"-20 allthread for the stud. I used a punch to damage
the bottom thread so the stud would stop at the bottom:

[![]({{ site.url }}/images/2015-04-26/image-0002.jpg)]({{ site.url}}/images/2015-04-26/image-0002.jpg)


 This shows the stud being stopped. If it works its way through, I just bang
on it some more!

[![]({{ site.url }}/images/2015-04-26/image-0003.jpg)]({{ site.url}}/images/2015-04-26/image-0003.jpg)


4 clamps seems to work quite well for holding sheet stock down.

I started to cut a larger piece and my z-axis wound up dropping as it was
cutting. I forgot to take some photos, but this was the aftermath:

[![]({{ site.url }}/images/2015-04-26/image-0004.jpg)]({{ site.url}}/images/2015-04-26/image-0004.jpg)


After some vacuuming:

[![]({{ site.url }}/images/2015-04-26/image-0005.jpg)]({{ site.url}}/images/2015-04-26/image-0005.jpg)


This was caused because the z-axis stepper was disabled while it was cutting,
and then the cutting forces wound up pulling the head deeper and deeper into
the cut.

I was running TinyG firmware version 438.02. I hooked up an LED to the Z-axis
enable line on the TinyG board and sure enough, I could see the stepper driver
being disabled while X & Y were still moving. I had the power management
setting for all 4 motors set to 2, which is supposed to keep the motor enabled
while any other axis is moving.



I asked about this over on the [ChiliPeppr Google Plus
group](https://plus.google.com/+DaveHylands/posts/fLbrV2yg8pY) and it seems it
was a firmware issue. So I downloaded the 440.14 firmware, flashed it, and
immediately lost all of my settings. Sigh.

That created another diversion, and I went off and wrote a python program for
archiving, restoring and viewing configuration files. You can find Config.py
[here](https://github.com/dhylands/TinyG-Utils/tree/master/Config). I've only
tested it under linux, but it should work under Windows and Mac as well. Let
me know if you have any suggestions, comments, issues, etc.

With the new firmware installed and my settings restored, I was able to cut
the piece, and the z-axis stepper stayed energized through the entire cut.
Here's a short video of the start of the cut:



That was cut with 1.5mm depth of cut 800 mm/sec travel, and max RPM (which I
believe is around 12,000 RPM). This was the finished cut.

[![]({{ site.url }}/images/2015-04-26/image-0006.jpg)]({{ site.url}}/images/2015-04-26/image-0006.jpg)


The flip side was white vinyl, and since I was using an up cut endmill, I put
the good side down so it would have a clean edge:

[![]({{ site.url }}/images/2015-04-26/image-0007.jpg)]({{ site.url}}/images/2015-04-26/image-0007.jpg)


That's all for now.

{% include ox-related.md %}
