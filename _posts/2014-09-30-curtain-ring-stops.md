---
layout: post
title: Curtain Ring Stops
date: '2014-09-30T19:42:00.002-07:00'
author: Dave Hylands
tags:
- OpenSCAD
- 3D-Printing
- Bukito
modified_time: '2014-09-30T19:43:28.217-07:00'
thumbnail: http://3.bp.blogspot.com/-K6F3enVuzdQ/VCtn28tRXDI/AAAAAAAAZCg/mhsMXajk1Ds/s72-c/4up.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-6824408900922457106
blogger_orig_url: http://blog.davehylands.com/2014/09/curtain-ring-stops.html
---

I learned a long time ago, that having cool toys (like my 3D printer) goes
over much better when I can make practical stuff for around the house.

So my very first real project was to print some curtain ring stops. Our
curtains have grommets to hold them on a rod, but the stop at the end of the
curtain rod is slightly smaller than the hole in the grommet. From time to
time, the curtain pops off the end of the rod. This doesn't bother me, I'm
6'-4" tall (1.93m for those metricized folks) and I just reach up and put it
back on. My wife, not being nearly as tall curses every time the curtain comes
off the end.

It takes about 12 minutes to print one disk (about 50mm diam and , so I ganged
them up and 3mm thick) and printed 4 at a time.

[![]({{ site.url }}/images/2014-09-30/image-0000.jpg)]({{ site.url}}/images/2014-09-30/image-0000.jpg)


Here's what the disk looks like when screwed onto the end cap:

[![]({{ site.url }}/images/2014-09-30/image-0001.jpg)]({{ site.url}}/images/2014-09-30/image-0001.jpg)

and what it looks like when installed:

[![]({{ site.url }}/images/2014-09-30/image-0002.jpg)]({{ site.url}}/images/2014-09-30/image-0002.jpg)

I've ordered some silver filament to print the disks for the living areas, and
will use the white ones (I ordered black, white and blue filament with my
printer) in my wife's sewing studio.

The disks are a fairly simple geometry, so I decided to model them using
OpenSCAD:



    translate([0, 0, 0]) {
     difference() {
      cylinder(h=3, r=25, center=true);
      cylinder(h=3, r=2.5, center=true);
     }
    }

    translate([60, 0, 0]) {
     difference() {
      cylinder(h=3, r=25, center=true);
      cylinder(h=3, r=2.5, center=true);
     }
    }

    translate([0, 60, 0]) {
     difference() {
      cylinder(h=3, r=25, center=true);
      cylinder(h=3, r=2.5, center=true);
     }
    }

    translate([0, 60, 0]) {
     difference() {
      cylinder(h=3, r=25, center=true);
      cylinder(h=3, r=2.5, center=true);
     }
    }

Next time I'll learn how to do for loops instead of copy/paste.

