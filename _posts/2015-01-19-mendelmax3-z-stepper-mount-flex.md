---
layout: post
title: MendelMax3 -  Z Stepper Mount Flex
date: '2015-01-19T08:51:00.000-08:00'
author: Dave Hylands
tags:
- MM3
modified_time: '2015-10-22T22:45:09.733-07:00'
thumbnail: http://1.bp.blogspot.com/-pWg7_m__0kg/VL0tVrAducI/AAAAAAAAdBY/oNqBEf9h2sw/s72-c/IMG_20150119_080907.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-4648404788571888880
blogger_orig_url: http://blog.davehylands.com/2015/01/mendelmax3-z-stepper-mount-flex.html
---

I suspected that there might be some flex in the Z stepper mount on my
MendelMax 3 given that it's a fairly thin piece of metal (0.050" or 1.3mm
powdercoated stainless steel):

[![]({{ site.url }}/images/2015-01-19/image-0000.jpg)]({{ site.url}}/images/2015-01-19/image-0000.jpg)



The first step was to see just how much deflection that existed. So I set up a
dial test indicator on the outside of the stepper mount, moved the gantry down
a bunch of steps, zeroed out the dial indicator and then started to move up in
increments of 0.1mm. I had a big ole chunk of steel that I rested on back
portion of the MM3, and used that to hold the magnetic base that held the
indicator:


Wow 0.09mm of deflection, mostly in the first 3-4 layers.

My gantry is setup with 2 direct drive extruders, which means that there is a
fair amount of weight being moved up and down on the Z axis.

From what I had heard, the MM2 used thicker aluminium parts. I also discovered
that [OpenBuildsPartStore](http://openbuildspartstore.com/) sold a [NEMA 17
stepper mount](http://openbuildspartstore.com/motor-mount-plate-nema-17/) that
could be adapted to work. It appears to be 0.125" (3.16mm) aluminum:

[![]({{ site.url }}/images/2015-01-19/image-0001.jpg)]({{ site.url}}/images/2015-01-19/image-0001.jpg)




I used an X-acto knife to score a line 20mm from the edge, cut along the line
using a hacksaw (ok - not really - I used my metal bandsaw, but this could
easily be cut with a hacksaw) and cleaned up the cut edge with a file. For
mounting, I lined up one edge with the 2040 vertical extrusion, and squared
with the frame:

[![]({{ site.url }}/images/2015-01-19/image-0002.jpg)]({{ site.url}}/images/2015-01-19/image-0002.jpg)



I then repeated the same test using the OpenBuild stepper mount:



Much better, only 0.03mm deflection. I think that having some type of braced
mount, using a printed part (either by itself or as a reinforcement to one of
metal mounts), would yield even less deflection. I'll be following up with
another bog post in the future once I get a chance to try that out.

Make sure you read
[Part 2]({% post_url 2015-01-21-mendelmax3-z-stepper-mount-flex-part-2 %})
where MTW addressed the problem with some braces.

