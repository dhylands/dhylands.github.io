---
layout: post
title: MendelMax3 - Toolless Z adjustment
date: '2015-01-06T08:25:00.000-08:00'
author: Dave Hylands
tags:
- MM3
modified_time: '2016-02-13T14:48:14.643-08:00'
thumbnail: https://2.bp.blogspot.com/-9Pzp-ViycuI/VKuGQZGMHaI/AAAAAAAAcds/yKQAIagNTL8/s72-c/IMG_20150105_222622.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-2127302159538741550
blogger_orig_url: http://blog.davehylands.com/2015/01/mendelmax3-toolless-z-adjustment.html
---

On my MendelMax 3, the Z endstop has a really short printed piece and a really
long bolt.

[![]({{ site.url}}/images/2015-01-06/image-0000.jpg)]({{ site.url}}/images/2015-01-06/image-0000.jpg)

The bolt has a phillips head, while all of the rest of the harware on the
MendelMax 3 is hex.

After making numerous adjustments (in retrospect, this turns out to be due to
my Z axis dropping, but that's another blog post), I wound up stripping the
threads in the printed piece.

Rather than just print up another one of the included printed piece, I decided
to print a larger piece which would incorporate a metal nut, be closer to the
endstop switch, and also allow for toolless adjustment.

I lined up the adjustment screw with the button on the microswitch, which
allows the lever to be removed. You can remove the lever by squeezing the end
together:

[![]({{ site.url}}/images/2015-01-06/image-0001.jpg)]({{ site.url}}/images/2015-01-06/image-0001.jpg)

Here are the parts (after printing, I lengthened the main piece by an
additional 5mm):

[![]({{ site.url}}/images/2015-01-06/image-0002.jpg)]({{ site.url}}/images/2015-01-06/image-0002.jpg)

The knob is a press fit ont the end of the bolt. I used a hexagon rather than
a circle because the hexagon is more dimensionally accurate (See [this
article](http://hydraraptor.blogspot.ca/2011/02/polyholes.html) for a detailed
discussion). I cheated and just use a six-sided piece, since the inner hexagon
is what actually turns the bolt.

[![]({{ site.url}}/images/2015-01-06/image-0003.jpg)]({{ site.url}}/images/2015-01-06/image-0003.jpg)

Bolt pressed into the knob:

[![]({{ site.url}}/images/2015-01-06/image-0004.jpg)]({{ site.url}}/images/2015-01-06/image-0004.jpg)

Here's the nut pressed into the bottom. I also filed the rim off the bolt so
that the bottom of the bolt is relatively flat.

[![]({{ site.url }}/images/2015-01-06/image-0005.jpg)]({{ site.url }}/images/2015-01-06/image-0005.jpg)

Here's everything assembled together. You could also use a locking lever from
my [Toolless Levelling post]({% post_url 2015-01-05-mendelmax3-toolless-levelling %}),
instead of a spring.

[![]({{ site.url}}/images/2015-01-06/image-0006.jpg)]({{ site.url}}/images/2015-01-06/image-0006.jpg)

[![]({{ site.url}}/images/2015-01-06/image-0007.jpg)]({{ site.url}}/images/2015-01-06/image-0007.jpg)

Here it is installed (this is the tweaked version which is 5mm lower than the
ones pictured above):

[![]({{ site.url}}/images/2015-01-06/image-0008.jpg)]({{ site.url}}/images/2015-01-06/image-0008.jpg)

You can find my FreeCAD and STL files
[here](http://www.thingiverse.com/thing:1340511).
