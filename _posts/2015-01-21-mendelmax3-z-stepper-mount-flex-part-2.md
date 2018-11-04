---
layout: post
title: MendelMax3 - Z Stepper Mount Flex - Part 2
date: '2015-01-21T10:27:00.001-08:00'
author: Dave Hylands
tags:
- MM3
modified_time: '2015-10-22T22:47:32.530-07:00'
thumbnail: https://i.ytimg.com/vi/7kxlhmPO-RA/0.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-6883749739177380420
blogger_orig_url: http://blog.davehylands.com/2015/01/mendelmax3-z-stepper-mount-flex-part-2.html
---

After discovering the
[flex in my Z axis]({% post_url 2015-01-19-mendelmax3-z-stepper-mount-flex %}),
I decided to see whether the flex was present just by moving the
X-axis. I wrote the following snippet of gcode:



    G28 X0
    G1 X250 F3600
    G1 X10  F3600
    ...repeat the above 2 lines 10 more times...

and this is what I saw (with the original MTW mounts):



I decided to design a brace, which looks like this:

[![]({{ site.url }}/images/2015-01-21/image-0000.jpg)]({{ site.url}}/images/2015-01-21/image-0000.jpg)



It's designed to fit under the existing mounting plate:

[![]({{ site.url }}/images/2015-01-21/image-0001.jpg)]({{ site.url}}/images/2015-01-21/image-0001.jpg)



And installs like this:

[![]({{ site.url }}/images/2015-01-21/image-0002.jpg)]({{ site.url}}/images/2015-01-21/image-0002.jpg)



Now I get virtually no deflection:



About a day after I designed this, the MTW folks came up with a much simpler,
easier/faster to print version:

[![]({{ site.url }}/images/2015-01-21/image-0003.jpg)]({{ site.url}}/images/2015-01-21/image-0003.jpg)



[![]({{ site.url }}/images/2015-01-21/image-0004.jpg)]({{ site.url}}/images/2015-01-21/image-0004.jpg)



These perform almost as good as mine, but are easier to install. Here's a
video showing the deflection while moving the X gantry back and forth (sorry -
it's slightly blurry):


I decided to use the MTW version due to end switch interference with my mount.

To summarize:

  * 0.1mm deflection using the MTW mount that came with the printer.
  * 0.03mm deflection  using the modified OpenBuild mount.
  * 0.01mm deflection using the MTW mount with the printed MTW braces.
  * 0.005mm deflection using the MTW mount with my heavy duty brace.

The MTW braces are available
[here](https://www.dropbox.com/s/klxkb14t8364znt/Z%20Deflection%20Limiter%20Pair.stl?dl=0).

My heavy duty brace is available [here](http://sproutform.com/physibles/165).
I don't recommend using this because it has some fit problems (it interferes
with the Z end stop).


