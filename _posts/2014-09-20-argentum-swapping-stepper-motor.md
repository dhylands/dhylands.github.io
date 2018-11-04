---
layout: post
title: Argentum - Swapping stepper motor direction
date: '2014-09-20T10:28:00.002-07:00'
author: Dave Hylands
tags:
- Argentum
- Electronics
modified_time: '2014-09-20T10:29:15.561-07:00'
thumbnail: https://i.ytimg.com/vi/oHXvsbm5PaI/0.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-9010931366420578794
blogger_orig_url: http://blog.davehylands.com/2014/09/argentum-swapping-stepper-motor.html
---

The Argentum has a nifty calibration routine where you stick the head in the
middle, and then it figures out which way the steppers are wired up by which
limit switches are hit.

However, their algorithim is still a big buggy. The calibration routine seemed
to work fine when the head was in the middle (no limit switches activated),
but had some issues if it started with one of the X-axis switches acivated:



Upgrading the firmware from the 0.12 version that came with the printer to
0.14 seems to have resolved that. However, I discovered an issue if you tried
to calibrate while the head was in the home position (Y limit switch
activtated):

When it starts out and the limit switch is activated, then it tries moving
very slowly for a short period of time, since it doesn't know which way the
head is moving (towards or away from the limit switch). However, since I had
previously done a calibration (which it remembers), it should have tried to do
its initial move away from the switch rather than towards it.

Since I didn't like the noises the machine was making while this happens, I
decided to swap the direction of the Y axis. These are bipolar steppers being
used, so you only need to swap the wires on one of the two coils to get the
stepper to go in the other direction.

Here's a photo of my Y-axis connector, as it arrived:

[![]({{ site.url }}/images/2014-09-20/image-0100.jpg)]({{ site.url}}/images/2014-09-20/image-0100.jpg)

The Argentum came with a nice little screwdriver package, that included a
variety of 1/8" bits. The torx T3 bit was small enough to fit through the
rectangular hole in the housing and depress the metal tab which allows the
wire to be released. Here's what the clip looks like once its outside of the
housing:



[![]({{ site.url }}/images/2014-09-20/image-0101.jpg)]({{ site.url}}/images/2014-09-20/image-0101.jpg)

Once the metal tab is flattened, you can start to pull the wire out. I did
this with the yellow wire, and then the blue wire. Once both wires are
started, you can pull completely out of the housing, swap them and reinsert:

[![]({{ site.url }}/images/2014-09-20/image-0102.jpg)]({{ site.url}}/images/2014-09-20/image-0102.jpg)

 Make sure you insert both wires far enough that the metal tab re-engage to
keep them in the housing.

Now the y axis moves in the opposite direction, and calibration routine works
properly even when starting from the home position.






