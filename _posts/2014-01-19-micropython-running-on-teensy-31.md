---
layout: post
title: MicroPython running on a Teensy 3.1 controlling a DragonTail
date: '2014-01-19T13:30:00.001-08:00'
author: Dave Hylands
tags:
- MicroPython
- Software
modified_time: '2014-06-15T10:16:36.088-07:00'
thumbnail: http://2.bp.blogspot.com/-bULfJlBhTNE/UtxB_YXWO1I/AAAAAAAAUqM/3PI568qaGvE/s72-c/DragonTail-Bot.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-2199455919442874502
blogger_orig_url: http://blog.davehylands.com/2014/01/micropython-running-on-teensy-31.html
---

I signed up for the [MicroPython
Kickstarter](https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers)
with the idea that it would be cool to use python
for low-level control of a robot.

While I'm waiting for the MicroPython board to arrive, I started to play with
a [Teensy 3.1](https://pjrc.com/store/teensy31.html), which is a small 32-bit
ARM based controller with 256K of flash and 64K of RAM.

I decided to try to port MicroPython to run on the teensy, and most of my
progress so far has been checked into the [MicroPython github
repoitory](https://github.com/micropython/micropython).

Wanting to see a robot running MicroPython, I put together the Solarbotics
DragonTail Deluxe Kit along with the
[Electronics Bundle](https://solarbotics.com/product/60135/), but I replaced
the Arduino controller with the Teensy 3.1.

Here's a photo of the bot:

[![]({{ site.url }}/images/2014-01-19/image-0000.jpg)]({{ site.url}}/images/2014-01-19/image-0000.jpg)





An this is a closeup of the Teensy 3.1 Breakout I whipped up:


[![]({{ site.url }}/images/2014-01-19/image-0001.jpg)]({{ site.url}}/images/2014-01-19/image-0001.jpg)


The header strips are GVS (Ground-Voltage-Signal). The outermost row is
ground, the middle row is 5v, and the inside row is signal. Since most of the
signals on the top side (relative to the picture) are analog, I made the
ground on that side be AGND. The jumper just to the left of green LED allows
me to connect the digital ground through to the analog ground if I need to.
The small green board in the bottom right is a [DC-DC Switching
Regulator](https://www.ebay.com/itm/NEW-Mini-DC-DC-Converter-Step-Down-Module-Adjustable-Power-Supply-Output-1-3-17V-/360741066304?ssPageName=ADME:L:OC:CA:3160) I got on eBay.

I put a short video of the bot running on
[YouTube](https://www.youtube.com/watch?v=AuMY1aiAN4k).

The [python
source](https://github.com/dhylands/DragonTail/blob/master/memzip_files/src/Dragon.py)
running under MicroPython can be found in my [DragonTail github
repository](https://github.com/dhylands/DragonTail).

