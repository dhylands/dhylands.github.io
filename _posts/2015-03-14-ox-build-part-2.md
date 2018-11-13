---
layout: post
title: OX Build - Part 2
date: '2015-03-14T22:50:00.000-07:00'
author: Dave Hylands
tags:
- OX
modified_time: '2015-11-01T17:57:33.106-08:00'
thumbnail: http://1.bp.blogspot.com/-NDTk6QySy_U/VQURlwfgb7I/AAAAAAAAfdc/nVLUd84GOrI/s72-c/IMG_20150314_151451.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-3143176722329338392
blogger_orig_url: http://blog.davehylands.com/2015/03/ox-build-part-2.html
---

NOTE: I recommend changing the order of things a bit. I mentioned this in
[part 3]({% post_url 2015-03-16-ox-build-part-3 %}) but I
thought I would edit my Part 2 post to mention that. Basically, I think that
its easier to assemble the entire Z-assembly, put the X-axis extrusions
through it and then mount that whole thing on the side plates.

Anways, on with the original post...

{% include ox-related.md %}

When squaring up the gantry, you want the front face of the gantry to be
perpendicular to the bed:

[![]({{ site.url }}/images/2015-03-14/image-0000.jpg)]({{ site.url}}/images/2015-03-14/image-0000.jpg)


The corner brackets have nubs on both faces, and one set of nubs needs to be
filed off.

[![]({{ site.url }}/images/2015-03-14/image-0001.jpg)]({{ site.url}}/images/2015-03-14/image-0001.jpg)


Otherwise it doesn't mate with the plate:

[![]({{ site.url }}/images/2015-03-14/image-0002.jpg)]({{ site.url}}/images/2015-03-14/image-0002.jpg)

This is the bracket with the nubs filed off:

[![]({{ site.url }}/images/2015-03-14/image-0003.jpg)]({{ site.url}}/images/2015-03-14/image-0003.jpg)



Which fits much better.

[![]({{ site.url }}/images/2015-03-14/image-0004.jpg)]({{ site.url}}/images/2015-03-14/image-0004.jpg)


Here's the left side of the Z axis (with the eccentrics):

[![]({{ site.url }}/images/2015-03-14/image-0005.jpg)]({{ site.url}}/images/2015-03-14/image-0005.jpg)


And the right side with the regular spacers.

[![]({{ site.url }}/images/2015-03-14/image-0006.jpg)]({{ site.url}}/images/2015-03-14/image-0006.jpg)


Once again, even ith the eccentrics at the loosest, I had difficulty getting
the extrusion on, and when I did get it on, it was very stiff. Fortunately,
there was enough slop in the screw holes, that if I loosened everything off
and then retightened, the axis finally moved without much effort.

[![]({{ site.url }}/images/2015-03-14/image-0007.jpg)]({{ site.url}}/images/2015-03-14/image-0007.jpg)


For assembling the remaining wheels, I found it easier to do all 4 at the same
time (note that there is a full spacer and a 3mm spacer between the wheels):

[![]({{ site.url }}/images/2015-03-14/image-0008.jpg)]({{ site.url}}/images/2015-03-14/image-0008.jpg)


Keep the back nuts loose and then you can hang this on the gantry.

[![]({{ site.url }}/images/2015-03-14/image-0009.jpg)]({{ site.url}}/images/2015-03-14/image-0009.jpg)


There was no way I could get the bottom bolts in with the 2 bottom wheels.
This picture showss the problem using the 20x60 for the  axis. It just doesn't
fit. I downloaded the DXF for the plates, and the holes in the plates I got
were bang on with the measurements from the DXF, so I have to conclude that
the poly wheels are just a wee bit bigger or wider than the delrin wheels.

I wound up drilling the 4 eccentric holes out with an 8.5mm drill before I
could get everything to fit (the holes in the DXF or 0.281" or 7.14mm). I
decided to drill the holes out rather than filing since the holes were already
in a consistent position an I felt drilling would more consistently enlarge
the holes versus filing.

[![]({{ site.url }}/images/2015-03-14/image-0010.jpg)]({{ site.url}}/images/2015-03-14/image-0010.jpg)


Using a mirror helps to get everything in place. Having the upper 4 nuts
extremely loose also helps (there is an eccentric on each side, so you want
the plates loose enough that you move the plate over the eccentric.

[![]({{ site.url }}/images/2015-03-14/image-0011.jpg)]({{ site.url}}/images/2015-03-14/image-0011.jpg)


The manual that came with my OX suggested putting the 90's in the top row. I
decided to put them in the middle row instead.

[![]({{ site.url }}/images/2015-03-14/image-0012.jpg)]({{ site.url}}/images/2015-03-14/image-0012.jpg)


I lowered the stepper to the lowest position that I could with the allen
wrench on top of the extrusion:

[![]({{ site.url }}/images/2015-03-14/image-0013.jpg)]({{ site.url}}/images/2015-03-14/image-0013.jpg)


With the bracket in the middle and the stepper lowered, I got a little more
movement in X-axis. If I ever remake my x plates, I'll take a bit more off
near the middle so that the X plate can come all of the way over to the side.

[![]({{ site.url }}/images/2015-03-14/image-0014.jpg)]({{ site.url}}/images/2015-03-14/image-0014.jpg)


Here's the X gantry in place:

[![]({{ site.url }}/images/2015-03-14/image-0015.jpg)]({{ site.url}}/images/2015-03-14/image-0015.jpg)


When I opened up my bags with the bearings in it, I discovered that they had
literally fallen apart. I machined up some Delrin replacements on my lathe,
figuring that they would work until I got replacements, and then I remembered
that I had some thrust bearings. The thrust bearings are the right size and
more appropriate for this application than radial bearings anyways.

[![]({{ site.url }}/images/2015-03-14/image-0016.jpg)]({{ site.url}}/images/2015-03-14/image-0016.jpg)


Footnote: I heard from Brandon at SMW3D that they switched bearing suppliers
after seeing this post, and he sent me replacement bearings from the new
supplier. The new bearings look good, so I thought that deserved a special
mention.

Trying to get the poly wheels to fit wound up taking a while, so that's as far
as I got today.

{% include ox-related.md %}
