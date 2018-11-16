---
layout: post
title: OX Build - Part 3
date: '2015-03-16T00:46:00.000-07:00'
author: Dave Hylands
tags:
- OX
modified_time: '2015-11-01T17:57:57.543-08:00'
thumbnail: http://2.bp.blogspot.com/-UUHy2SFFm_Y/VQZoQtDF5dI/AAAAAAAAfp8/lusqAkG0Htk/s72-c/IMG_20150315_122021~2.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-7873849363613409679
blogger_orig_url: http://blog.davehylands.com/2015/03/ox-build-part-3.html
---

After getting things together up to the end of Part 2, I think that things
should be assembled in a slightly different order.

{% include ox-related.md %}

I didn't tighten the screws down on my delrin nut because I wanted to do it
with the leadscrew installed. I found working on the Z axis to be alot more
difficult than it needed to be, just because it was mounted on the gantry.

So I think that the entire Z axis assembly should be assembled first, then
mounted on the gantry extrusions and screw the whole thing down.

I had issues getting my leadscrew to go through the delrin nut. I could start
it, but couldn't seem to get it to go all the way through. Looking into the
nut I could see pieces of swarf still floating around:


[![]({{ site.url }}/images/2015-03-16/image-0000.jpg)]({{ site.url}}/images/2015-03-16/image-0000.jpg)


I removed what swarf I could see with a pair of tweezers. Then I was able to
get the leadscrew through, and a bunch more swarf came out:

[![]({{ site.url }}/images/2015-03-16/image-0001.jpg)]({{ site.url}}/images/2015-03-16/image-0001.jpg)


I then ran the leadscrew through several more times. This is a shot of what
came out (not including the bigger pieces I pulled out with the tweezers:

[![]({{ site.url }}/images/2015-03-16/image-0002.jpg)]({{ site.url}}/images/2015-03-16/image-0002.jpg)


Remove the delrin nut and put it on the leadscrew. You'll need to install the
upper bearing and the locking collar first. Leave the 3 screws which mount the
plate stepper plate to the extrusion slightly loose. Leave the 2 nylock nuts
in the delrin nut (they should be on the side facing the extrusion).

[![]({{ site.url }}/images/2015-03-16/image-0003.jpg)]({{ site.url}}/images/2015-03-16/image-0003.jpg)


Slide the extrusion into place:

[![]({{ site.url }}/images/2015-03-16/image-0004.jpg)]({{ site.url}}/images/2015-03-16/image-0004.jpg)


Line up the holes and put the leadscrew nuts in place. Tighten them up almost
all the way, but leave them just a wee bit loose.

[![]({{ site.url }}/images/2015-03-16/image-0005.jpg)]({{ site.url}}/images/2015-03-16/image-0005.jpg)


Now turn the leadscrew so that the extrusion is as close to the stepper end a
possible, without actually touching the black mounting plate. Tighten up the
screws on the mounting plate, taking care to keep the straight edge of the
black plate parallel to the face of the extrusion. You're also looking to have
the leadscrew parallel with the back of the extrusion. This is the black edge
I was talking about:

[![]({{ site.url }}/images/2015-03-16/image-0006.jpg)]({{ site.url}}/images/2015-03-16/image-0006.jpg)



I found that looking through the holes between the mounting screws, you'll be
able to see part of the extrusion. In my photo below, none of the extrusion
was visible.

[![]({{ site.url }}/images/2015-03-16/image-0007.jpg)]({{ site.url}}/images/2015-03-16/image-0007.jpg)


Now put the bottom black plate on and move the extrusion up (by rotating the
leadscrew) until the bottom plate is almost touching the front plate, and
tighten up the screws.

Make sure that the bearings fit into the recess in the black plate, and secure
the lock collar. Make sure that they is no play between the lock collars and
the bearings.

Now you can remount the z axis assembly on the extrusions and mount the
extrusions.

[![]({{ site.url }}/images/2015-03-16/image-0008.jpg)]({{ site.url}}/images/2015-03-16/image-0008.jpg)


I verified that the front of the z-axis was sqaure with the bed while
tightening the screws up.

[![]({{ site.url }}/images/2015-03-16/image-0009.jpg)]({{ site.url}}/images/2015-03-16/image-0009.jpg)



Time for the belts. I filed the ridges off the edges of the bolts that were
going to be used to securing the belts. With the ridges things tend to move as
the screws are tightened.

[![]({{ site.url }}/images/2015-03-16/image-0010.jpg)]({{ site.url}}/images/2015-03-16/image-0010.jpg)


I found the easiest way to hold the screws while filing the ends was to put
the screws in my allen wrench and then hold the screw with my thumb and finger
while my hand was wrapped around the allen wrench:

[![]({{ site.url }}/images/2015-03-16/image-0011.jpg)]({{ site.url}}/images/2015-03-16/image-0011.jpg)


I also didn't like the screws clamping directly on the belts. I had some
Simpson Strong Tie metal plates that were about 0.036" or 0.9mm thick).

[![]({{ site.url }}/images/2015-03-16/image-0012.jpg)]({{ site.url}}/images/2015-03-16/image-0012.jpg)


I cut a piece about 5mm wide and the same width of a T-nut.

[![]({{ site.url }}/images/2015-03-16/image-0013.jpg)]({{ site.url}}/images/2015-03-16/image-0013.jpg)


I put these between the T-nut and and the belt, so that the screw was clamping
on the metal shim instead of directly on the belt.

The instructions use drop in nuts for the X axis belt, so I did that, but I
think I would have preferred to use the regular T-nut and shims.

I'd like to put belt tensioners on all of the belts, so then this will be
pretty much a moot point.

Tip: don't use ball end allen wrenches for tightening up the grub screws.

[![]({{ site.url }}/images/2015-03-16/image-0014.jpg)]({{ site.url}}/images/2015-03-16/image-0014.jpg)



I twisted one of mine right off. I could move it around but couldn't get it
out. Even gravity wasn't being helpful. Then I tried a stack of rare earth
magnets and they pulled it right out (phew):

[![]({{ site.url }}/images/2015-03-16/image-0015.jpg)]({{ site.url}}/images/2015-03-16/image-0015.jpg)


Brandon (from [hobby-fab](https://www.hobby-fab.com/)) asked me to check my speed
controller (since he was going to be sending me replacement bearings -
apparently somebody else had a speed controller that went bad.

I wired everything up:

[![]({{ site.url }}/images/2015-03-16/image-0016.jpg)]({{ site.url}}/images/2015-03-16/image-0016.jpg)



[![]({{ site.url }}/images/2015-03-16/image-0017.jpg)]({{ site.url}}/images/2015-03-16/image-0017.jpg)


And pluugged it in. The spindle would start turning and immediately stop. The
power supply seemed to be cutting out.

Doh:

[![]({{ site.url }}/images/2015-03-16/image-0018.jpg)]({{ site.url}}/images/2015-03-16/image-0018.jpg)


I had checked the 24V supply when I unpacked everything but neglected to check
the 48V supply, and it was set to 230V.

I changed it to 115V:

[![]({{ site.url }}/images/2015-03-16/image-0019.jpg)]({{ site.url}}/images/2015-03-16/image-0019.jpg)



and lo and behold, it worked!

I took a video of the Quiet Cut spindle:


 And also from my Bosch 1619EV router that I use for normal woodworking:


That's it for this part. Next will be the wiring.

{% include ox-related.md %}
