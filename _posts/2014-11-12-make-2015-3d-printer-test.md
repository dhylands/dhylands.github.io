---
layout: post
title: Make 2015 3D Printer Test
date: '2014-11-12T18:13:00.001-08:00'
author: Dave Hylands
tags:
- 3D-Printing
- Bukito
modified_time: '2014-11-18T22:49:42.390-08:00'
thumbnail: https://4.bp.blogspot.com/-BGdROVqKNAI/VGQGB3rXQqI/AAAAAAAAad8/Xck0qAKAn2w/s72-c/IMG_20141112_171245%7E2.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-3472543958984926256
blogger_orig_url: http://blog.davehylands.com/2014/11/make-2015-3d-printer-test.html
---

Make recently published their 2015 3D Printer test results and they also
published the test files they used and how to evaluate them.
https://makezine.com/2014/11/07/how-to-evaluate-the-2015-make-3dp-test-probes/

I decided to try on my Bukito and I've documented what I got here.

The Bukito was also scored on Page 61, so I thought it would be interesting to
compare my scores to the magazine scores. I have the PLA cooling fan (with the
optional duct( and the magazine model didn't, so I think that contributed to
some of the lower scores in the magazine.


I was using [1.75mm Gray filament]https://seacans.com/collections/pla/products/pla-grey-1-75mm-1kg?variant=845014559) that I purchased from
[seacans.com](https://seacans.com/)

I sliced the models in Cura. This is my [settings
file](https://www.dropbox.com/s/nh07ew339t384sk/Make-2015-Tests-Cura-PLA.ini?dl=0).

Here are my settings changes:

  * Layer Height 0.2mm
  * Printing Speed 30 mm/sec (although for many of these the actual printing speed was much slower due to the small size of the layers).
  * I printed the first layer at 210C, and then dropped the temp to 190C for the remaining layers.
  * I changed the first layer height to 0.2mm and 100% extrusion width.

#### Dimensional Accuracy:

[![]({{ site.url}}/images/2014-11-12/image-0000.jpg)]({{ site.url}}/images/2014-11-12/image-0000.jpg)![]({{
site.url }}/images/2014-11-12/image-0001.jpg)


Time: 00:38:08
My Score: 5 - I didn't count the seam. 4 If I count the seam.
Magazine Score: 4

X Measurement: 19.94 mm
Y Measurement: 20.05mm There was a seam right on the Y axis - you can see it
just left of center in the photo on the left. On the seam I measured 20.18 mm.
So I think I'm over extruding just a touch.

I can also see some Z-axis artifacts (my z-axis has 1 mm thread).


#### Bridging:

[![]({{ site.url}}/images/2014-11-12/image-0002.jpg)]({{ site.url}}/images/2014-11-12/image-0002.jpg)



[![]({{ site.url}}/images/2014-11-12/image-0003.jpg)]({{ site.url}}/images/2014-11-12/image-0003.jpg)


Time: 00:48:21
My Score:  Based on the description, I think this is a 4 or 5. The droops were
all less than 2mm.
Magazine Score: 2

#### Overhang:

[![]({{ site.url}}/images/2014-11-12/image-0004.jpg)]({{ site.url}}/images/2014-11-12/image-0004.jpg)[![]({{site.url}}/images/2014-11-12/image-0005.jpg)]({{site.url}}/images/2014-11-12/image-0005.jpg)


Time: 01:27:00
My Score:  4
Magazine Score: 2

The 70 degree overhand wasn't pretty on the back, but no drops.

UPDATE: I rotated the model 90 degrees and got much better results. See
[this]({% post_url 2014-11-18-orientation-matters-when-printing-with %}) post.

#### Negative Space Tolerance:

[![]({{ site.url}}/images/2014-11-12/image-0006.jpg)]({{ site.url}}/images/2014-11-12/image-0006.jpg)


Time: 00:52:41
My Score: 4
Magazine Score: 2

I printed this a couple of times. One time, all of the pegs came out, another
time, the smallest clearance peg won't come out. I can see it moving, but
there is something inside holding it in.


#### Fine Positive Space Features Performance:





[![]({{ site.url}}/images/2014-11-12/image-0007.jpg)]({{ site.url}}/images/2014-11-12/image-0007.jpg)

Time: 00:25:05
My Score: 3
Magazine Score: 3


#### Mechanical Resonance in XY:

[![]({{ site.url}}/images/2014-11-12/image-0008.jpg)]({{ site.url}}/images/2014-11-12/image-0008.jpg)

Time: 00:38:33
My Score: Pass - no rippling. If I printed at 100 mm/sec then I know I would
see some rippling. There was some slight over extrusion on the left-hand
corner (seam location). The remaining corners all looked really good.
Magazine Score: Pass

I wound up using the model with 1mm walls. I see a faint herringbone pattern
which I think comes from the fact that the synchromesh goes over a pair of
bearings at the end rather than over a proper synchromesh pulley (like the one
on the stepper motor). I see the same pattern on both X & Y.

[![]({{ site.url }}/images/2014-11-12/image-0009.jpg)](({{ site.url }}/images/2014-11-12/image-0009.jpg)
[![]({{ site.url }}/images/2014-11-12/image-0010.jpg)](({{ site.url }}/images/2014-11-12/image-0010.jpg)

The photo on the left shows the synchromesh going over the bearing, and the
photo on the right shows the synchromesh pulley.


#### Mechanical Resonance in Z:



[![]({{ site.url}}/images/2014-11-12/image-0011.jpg)]({{ site.url}}/images/2014-11-12/image-0011.jpg)


Time: 01:29:49
My Score: Pass
Magazine Score: Pass

I couldn't see any of the Z artifacts on this print that I could see on some
of the other prints.

I also printed the [Maker Faire Robot Action
Figure](https://makezine.com/2014/11/10/print-in-place-the-additive-holy-grail/)
and all of the joints move:

[![]({{ site.url}}/images/2014-11-12/image-0012.jpg)]({{ site.url}}/images/2014-11-12/image-0012.jpg)[![]({{site.url}}/images/2014-11-12/image-0013.jpg)]({{site.url}}/images/2014-11-12/image-0013.jpg)


There was a little big of sagging under the arms, but everything else seems to
be good.

