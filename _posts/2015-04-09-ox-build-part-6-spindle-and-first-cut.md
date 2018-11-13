---
layout: post
title: OX Build - Part 6 - Spindle and First Cut
date: '2015-04-09T00:49:00.001-07:00'
author: Dave Hylands
tags:
- OX
modified_time: '2015-11-01T17:59:28.112-08:00'
thumbnail: http://2.bp.blogspot.com/-XOWF15CkevU/VSNq-rP-h8I/AAAAAAAAgjs/b8wMmPUPnVw/s72-c/image.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-5894718804736970295
blogger_orig_url: http://blog.davehylands.com/2015/04/ox-build-part-6-spindle-and-first-cut.html
---

Since I decided to change my Z-axis bearings to proper thrust bearings, I was
concerned about getting dust in the bearings.
[![]({{ site.url }}/images/2015-04-09/image-0000.jpg)]({{ site.url}}/images/2015-04-09/image-0000.jpg)

{% include ox-related.md %}

Here's a side view of the thrust bearing:

[![]({{ site.url }}/images/2015-04-09/image-0001.jpg)]({{ site.url}}/images/2015-04-09/image-0001.jpg)


I also noticed that the leadscrew was projecting below the bottom of the
z-axis:

[![]({{ site.url }}/images/2015-04-09/image-0002.jpg)]({{ site.url}}/images/2015-04-09/image-0002.jpg)


I also noticed my TinyG hanging below the cross bar, so I'll need to fix that
as well. I wouldn't want that to catch a clamp. I cut the bottom piece off the
end of the leadscrew and printed an end cap and some shields for the thrust
bearings:

[![]({{ site.url }}/images/2015-04-09/image-0003.jpg)]({{ site.url}}/images/2015-04-09/image-0003.jpg)


The endcap worked out great, but I had to make a few more refinements to the
other 2 pieces in order to have the dust shields not hit the X gantry plate. I
forgot to take picttures of the new parts, but you can see the changes in the
STL files.

[![]({{ site.url }}/images/2015-04-09/image-0004.jpg)]({{ site.url}}/images/2015-04-09/image-0004.jpg)


I recessed the screw heads and used button head cap screws, making the dust
cap about the same thickness as the low profile screws used to hold the
adapter plate:

[![]({{ site.url }}/images/2015-04-09/image-0005.jpg)]({{ site.url}}/images/2015-04-09/image-0005.jpg)


This shows the thrust bearing inside the dust shield on the lower portion:

[![]({{ site.url }}/images/2015-04-09/image-0006.jpg)]({{ site.url}}/images/2015-04-09/image-0006.jpg)


And the upper portion:

[![]({{ site.url }}/images/2015-04-09/image-0007.jpg)]({{ site.url}}/images/2015-04-09/image-0007.jpg)


I printed up a spindle mount:

[![]({{ site.url }}/images/2015-04-09/image-0008.jpg)]({{ site.url}}/images/2015-04-09/image-0008.jpg)


After installing, I don't like the fact that the mounting screws are hidden
once the spindle is installed (but I'll fix that at a later time):

[![]({{ site.url }}/images/2015-04-09/image-0009.jpg)]({{ site.url}}/images/2015-04-09/image-0009.jpg)


Here it is with the spindle installed:

[![]({{ site.url }}/images/2015-04-09/image-0010.jpg)]({{ site.url}}/images/2015-04-09/image-0010.jpg)


And a video showing the Z rapids after a bit of tuning.


Ready to start cutting. Well almost. When I turned the spindle on, I totally
lost all of my comms with the TinyG board. I verified that the noise was being
introduced in the first cable chain. If I plugged the USB into the TinyG
directly then it worked fine. I had two unshielded twisted power lines, so my
first attempt to fix things was to replace the spindle power with a shielded
cable run. That improved things, but not completely. The USB connection would
bounce when the spindle was turned on, but would be usable after that.

I then looked closely at the USB cable I was using:

[![]({{ site.url }}/images/2015-04-09/image-0011.jpg)]({{ site.url}}/images/2015-04-09/image-0011.jpg)


The cable has shielding, but it doesn't seem to be connected to anything. Sure
enough, no connectivity from the shield on one end to the other.

I swapped in another USB cable. My multimeter confirmed that the shield was
connected through, and everything works.

[![]({{ site.url }}/images/2015-04-09/image-0012.jpg)]({{ site.url}}/images/2015-04-09/image-0012.jpg)


For my first part, I decided to try and create a T-nut out of some 1/4"
hardboard. I first designed the part in
[OnShape](https://cad.onshape.com/documents/0dabadcc2c7c4596a56f4e88/w/7a1a3f8be8b44ee196f4b830/e/bbd244280bd84c10be9876f0):

[![]({{ site.url }}/images/2015-04-09/image-0013.png)]({{ site.url}}/images/2015-04-09/image-0013.png)


I then created a sketch and "Used" (aka projected) all of the features onto it
and exported that sketch as a DXF. The orange lines are the projected
features:

[![]({{ site.url }}/images/2015-04-09/image-0014.png)]({{ site.url}}/images/2015-04-09/image-0014.png)



I then imported the DXF into CamBam. The white lines are the DXF features. I
added a pocket operation for the large recess, a pocket for the center hole
that goes through all of the way, and finally, added a profile operation for
the outline. CamBam supports tabs, so I added a tab on each side. These are
small unmachined pieces which are left behind to keep the main part from
moving while performing the very final operations. The tabs are represented by
the rectangles you can see. If you look at the toolpath (blue and green lines
except for the tabs) you can see that Z rises up to leave the tab behind:

[![]({{ site.url }}/images/2015-04-09/image-0015.png)]({{ site.url}}/images/2015-04-09/image-0015.png)


I used a 3.175mm endmill for all of the operations, 600 mm/min feedrate, 100
mm/min plunge rate. The recommended depth of cut for MDF is 50% of the tool
diameter, so I used numbers around 1.5mm for the depth increment, and for the
final profile I used a cut width of 4mm so that the first cut (which is full
width of the cutter) wasn't the final cut. The final cut would wind up being 4
- 3.175mm = 0.825mm, which will generally give a better finish than the finish
on a full width cut.

I then generated the gcode, and ran it through OpenSCAM to verify that
everything looked good:

[![]({{ site.url }}/images/2015-04-09/image-0016.png)]({{ site.url}}/images/2015-04-09/image-0016.png)


Here's a video of the first cut:


And a photo of the finished cut:

[![]({{ site.url }}/images/2015-04-09/image-0017.jpg)]({{ site.url}}/images/2015-04-09/image-0017.jpg)


And the spoiler board (I used some 1/8" hardboard). My total cut depth was
6.85mm for the 6.35mm (1/4") material:

[![]({{ site.url }}/images/2015-04-09/image-0018.jpg)]({{ site.url}}/images/2015-04-09/image-0018.jpg)


This shows the tabs:

[![]({{ site.url }}/images/2015-04-09/image-0019.jpg)]({{ site.url}}/images/2015-04-09/image-0019.jpg)


This is the T-nut cleaned up a bit:

[![]({{ site.url }}/images/2015-04-09/image-0020.jpg)]({{ site.url}}/images/2015-04-09/image-0020.jpg)


The metal propel nut didn't want to go in, so I woud up drilling 3 extra
holes:

[![]({{ site.url }}/images/2015-04-09/image-0021.jpg)]({{ site.url}}/images/2015-04-09/image-0021.jpg)


And now the propel nut goes in fine:

[![]({{ site.url }}/images/2015-04-09/image-0022.jpg)]({{ site.url}}/images/2015-04-09/image-0022.jpg)


So I'll have to modify my model to drill those 3 extra holes. Here's the T-nut
in the slot:

[![]({{ site.url }}/images/2015-04-09/image-0023.jpg)]({{ site.url}}/images/2015-04-09/image-0023.jpg)



I since discovered that you can import STLs into CamBam:

[![]({{ site.url }}/images/2015-04-09/image-0024.png)]({{ site.url}}/images/2015-04-09/image-0024.png)


which doesn't look all that impressive. However, if you select the Surface,
and then choose Edit->Surface->Edge Detect, and then delete the Surface
object, you'll wind up with this much nicer looking wire frame:

[![]({{ site.url }}/images/2015-04-09/image-0025.png)]({{ site.url}}/images/2015-04-09/image-0025.png)


And you can click on polylines from the wireframe to perform machining
operations with.

I used the 3D printed T-nuts, a few scraps of wood with drilled holes, some
all thread and knobs for my first clamps:

[![]({{ site.url }}/images/2015-04-09/image-0026.jpg)]({{ site.url}}/images/2015-04-09/image-0026.jpg)


I think my next project will be some decent clamps.


3D Printed Parts:

Dust Cover|
[OnShape](https://cad.onshape.com/documents/bd695a4a22c34d5b9a87a799/w/fe1c97c7dacb462abdb37b54/e/7b030486f55b42b8a4e5d66f)|
[STEP & STL](https://github.com/dhylands/3D-Printed-Parts/tree/master/OX/Dust-
Cover)
---|---|---
52mm Spindle Mount|
[OnShape](https://cad.onshape.com/documents/58088030d4b7419b8ad214f6/w/8420bcf6bbee4a0c8e7dbdd0/e/ed907d1f45ab434ab7380b54)|
[STEP & STL](https://github.com/dhylands/3D-Printed-Parts/tree/master/OX/52mm-
Spindle-Mount)

{% include ox-related.md %}
