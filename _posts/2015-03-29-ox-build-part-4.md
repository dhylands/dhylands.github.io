---
layout: post
title: OX Build - Part 4
date: '2015-03-29T10:49:00.000-07:00'
author: Dave Hylands
tags:
- OX
modified_time: '2015-11-01T17:58:29.945-08:00'
thumbnail: http://4.bp.blogspot.com/-irVpqLzvrAs/VReSFG1LH8I/AAAAAAAAgNM/K3g3UWdELiw/s72-c/IMG_20150317_072621~2.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-4280290516733099225
blogger_orig_url: http://blog.davehylands.com/2015/03/ox-build-part-4.html
---

Now that the basic mechanical stuff is done, it's on to the electronics.

{% include ox-related.md %}

I had some surplus cable chains that I salvaged off another machine, so the
first order of business was to create mounts for them. Right around this time,
I also discovered [onshape.com](https://onshape.com/) which is a free online
solid modelling CAD site. You need to request a beta invite. This took a day
for me, but other people I've talked to have gotten their accounts activated
fairly quickly.

In the event that any of the 3 printed parts are useful to someone, I'll be
making all of the parts public under OnShape, and will provide URLs to the
parts, to STEP files, and to the STL files. I'll put a table with links to all
of the 3D printed parts at the end of the post.

This is the lower X cable chain mount. This fits in the V-Slot.

[![]({{ site.url }}/images/2015-03-29/image-0000.jpg)]({{ site.url}}/images/2015-03-29/image-0000.jpg)



The upper X cable chain mount (goes above the stepper):

[![]({{ site.url }}/images/2015-03-29/image-0001.jpg)]({{ site.url}}/images/2015-03-29/image-0001.jpg)


Here's the X cable chain mounted:

[![]({{ site.url }}/images/2015-03-29/image-0002.jpg)]({{ site.url}}/images/2015-03-29/image-0002.jpg)


For the Y cable chain, I wanted something to support the cable chain. I used
two pieces of 90 degree trim pieces I found at Home Depot. This is the mount I
designed:

[![]({{ site.url }}/images/2015-03-29/image-0003.jpg)]({{ site.url}}/images/2015-03-29/image-0003.jpg)



This is what the 90 degree angle pieces look like (they're about 3/4" on each
side):

[![]({{ site.url }}/images/2015-03-29/image-0004.jpg)]({{ site.url}}/images/2015-03-29/image-0004.jpg)


The 90's fitted into the mounting piece:

[![]({{ site.url }}/images/2015-03-29/image-0005.jpg)]({{ site.url}}/images/2015-03-29/image-0005.jpg)


And the Y cable chain support in place:

[![]({{ site.url }}/images/2015-03-29/image-0006.jpg)]({{ site.url}}/images/2015-03-29/image-0006.jpg)


This is the upper mount for the Y cable chain:

[![]({{ site.url }}/images/2015-03-29/image-0007.jpg)]({{ site.url}}/images/2015-03-29/image-0007.jpg)


With the cable chain attached:

[![]({{ site.url }}/images/2015-03-29/image-0008.jpg)]({{ site.url}}/images/2015-03-29/image-0008.jpg)


And the lower mount. Since this is near the middle of the support, it also
helps to hold the 90 degree channels together as well.

[![]({{ site.url }}/images/2015-03-29/image-0009.jpg)]({{ site.url}}/images/2015-03-29/image-0009.jpg)


 Gantry all of the way back:

[![]({{ site.url }}/images/2015-03-29/image-0010.jpg)]({{ site.url}}/images/2015-03-29/image-0010.jpg)


Gantry all of the way forward:

[![]({{ site.url }}/images/2015-03-29/image-0011.jpg)]({{ site.url}}/images/2015-03-29/image-0011.jpg)


The cable chain for the Y axis was Igus Zipper chain, so one of the sides is
removable, which makes putting the cable in a bit easier:

[![]({{ site.url }}/images/2015-03-29/image-0012.jpg)]({{ site.url}}/images/2015-03-29/image-0012.jpg)


I printed a temporary mount for the TinyG board (I'll eventually use a metal
enclosure). The 4 holes in the middle will mount on the rear of the gantry.

[![]({{ site.url }}/images/2015-03-29/image-0013.jpg)]({{ site.url}}/images/2015-03-29/image-0013.jpg)


And the upper portion allows for a 12V 80mm cooling fan. The cooling fan
should really blow onto the back of the board, and I'll move things around
when I build the metal enclosure.

[![]({{ site.url }}/images/2015-03-29/image-0014.jpg)]({{ site.url}}/images/2015-03-29/image-0014.jpg)


The speed controller had a couple of places that looked like they could be
used for mounting holes, so I tapped them for M3:

[![]({{ site.url }}/images/2015-03-29/image-0015.jpg)]({{ site.url}}/images/2015-03-29/image-0015.jpg)


This is the mount for the speed controller:

[![]({{ site.url }}/images/2015-03-29/image-0016.jpg)]({{ site.url}}/images/2015-03-29/image-0016.jpg)


I also created some T-nut keepers, so I could put some extra T-nuts in the
slots nd not have them make vibration noise:

[![]({{ site.url }}/images/2015-03-29/image-0017.jpg)]({{ site.url}}/images/2015-03-29/image-0017.jpg)


This shows some of the T-nut keepers in use:

[![]({{ site.url }}/images/2015-03-29/image-0018.jpg)]({{ site.url}}/images/2015-03-29/image-0018.jpg)



Everything all wired up:

[![]({{ site.url }}/images/2015-03-29/image-0019.jpg)]({{ site.url}}/images/2015-03-29/image-0019.jpg)


Closeup of the left Y stepper:

[![]({{ site.url }}/images/2015-03-29/image-0020.jpg)]({{ site.url}}/images/2015-03-29/image-0020.jpg)


And the right Y stepper:

[![]({{ site.url }}/images/2015-03-29/image-0021.jpg)]({{ site.url}}/images/2015-03-29/image-0021.jpg)


The top of the X cable chain. I left a piece of string in the cable chain
since I still have more wires to pull through (this cable chain didn't have
the "zipper" feature). I used a zap strap to keep the cable loom from fraying
and then wrapped it in heat shrink.

[![]({{ site.url }}/images/2015-03-29/image-0022.jpg)]({{ site.url}}/images/2015-03-29/image-0022.jpg)


Here are some wire clips I designed. The one on the left is secured to the
V-Slot using an M5 screw. The one on the right snaps into the V-Slot:

[![]({{ site.url }}/images/2015-03-29/image-0023.jpg)]({{ site.url}}/images/2015-03-29/image-0023.jpg)


Here's an example of the screw mounted version:

[![]({{ site.url }}/images/2015-03-29/image-0024.jpg)]({{ site.url}}/images/2015-03-29/image-0024.jpg)


An the clip on version:

[![]({{ site.url }}/images/2015-03-29/image-0025.jpg)]({{ site.url}}/images/2015-03-29/image-0025.jpg)


Closeup of the stepper wiring. From left to right is Motor 1 thru 4, X, Y1, Z,
and Y2. I wired the NEMA 23 motors (X, Y1, and Y2) all in the same order. For
some reason, the NEMA 17 use different colors for the coil pairs, which is why
its different.

[![]({{ site.url }}/images/2015-03-29/image-0026.jpg)]({{ site.url}}/images/2015-03-29/image-0026.jpg)


I designed a pen mount, and this is a photo of the pen mount, along with the
output of the first gcode file run:

[![]({{ site.url }}/images/2015-03-29/image-0027.jpg)]({{ site.url}}/images/2015-03-29/image-0027.jpg)


Video clip showing the first gcode run using ChilPeppr:


I set the rapids to 400 mm/sec (24000 mm/min) and here's a video showing
corner to corner moves. That was just my initial guess at a rapid speed, I'll
need to play to find out how fast it can actually go.



3D Printed Parts

| OX-Cable-Chain-Mounts|[OnShape](https://cad.onshape.com/documents/eb4e2b01aaca4131bfc64adb/w/b580832dbaa945a1a5b07eb1) | [github (STEP & STL)](https://github.com/dhylands/3D-Printed-Parts/tree/master/OX/Cable-Chain-Mounts) |
| Spindle-Driver-Mount | [OnShape](https://cad.onshape.com/documents/a96ecf85f7a34e2a8763aafc/w/ba8e23a814c74d6d8dc1dfb7/e/15e9ed1c33b64cd9ba1d2d76) | [github (STEP & STL)](https://github.com/dhylands/3D-Printed-Parts/tree/master/OX/Spindle-Driver-Mount) |
| TinyG-Mount | [OnShape](https://cad.onshape.com/documents/229ddbdaf73a48eaaf120f7d/w/e085852e97c44a929d195efd/e/dbd6e75dcdc14f8897d6faa1) | [github (STEP & STL)](https://github.com/dhylands/3D-Printed-Parts/tree/master/OX/TinyG-Mount) |
| Wire-Clips | [OnShape](https://cad.onshape.com/documents/2bb479db69364fbbb4183eb9/w/06f3774923fa4ca2b0a4cfb0/e/5bb9567af54941a298dffa66) | [github (STEP & STL)](https://github.com/dhylands/3D-Printed-Parts/tree/master/V-Slot/Wire-Clips) |
| T-Nut-Keeper | [OnShape](https://cad.onshape.com/documents/fb7d8749f7824fc9a0b49831/w/ec96c86b68d1463c9896ab3b/e/be95df3d9ead4f3fbeb6c493) | [github (STEP & STL)](https://github.com/dhylands/3D-Printed-Parts/tree/master/V-Slot/T-Nut-Keeper) |
| Pen-Holder | [OnShape](https://cad.onshape.com/documents/1ab6b066f6d94400916b30d8/w/7a68bf29b63d4e1e9209e5da/e/2a07b34b57cf4736a098dee9) | [github (STEP & STL)](https://github.com/dhylands/3D-Printed-Parts/tree/master/OX/Pen-Holder) |

{% include ox-related.md %}
