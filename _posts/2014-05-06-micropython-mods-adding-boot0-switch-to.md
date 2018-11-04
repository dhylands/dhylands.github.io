---
layout: post
title: MicroPython mods - Adding a BOOT0 switch to the pyboard.
date: '2014-05-06T23:07:00.001-07:00'
author: Dave Hylands
tags:
- MicroPython
modified_time: '2014-06-15T10:14:20.618-07:00'
thumbnail: http://4.bp.blogspot.com/-_hO2wnGQUfs/U2nKH-_AwrI/AAAAAAAAVg0/YfVqQz0taSU/s72-c/Boot-Switch-800.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-7985888033366943262
blogger_orig_url: http://blog.davehylands.com/2014/05/micropython-mods-adding-boot0-switch-to.html
---

WooHoo - My [MicroPython](http://micropython.org/) board showed up today. Here
it is, enclosed in a [SliceCase](http://www.slicecase.com/).

[![]({{ site.url }}/images/2014-05-06/image-0000.jpg)]({{ site.url}}/images/2014-05-06/image-0000.jpg)

I also made my first mod, which was to add a switch for the BOOT1 signal. The
red wire runs to 3.3v (on one of the caps connected to pin 64), and the white
wire runs to the BOOT0 signal on R15 (See the bottom left corner of the
[schematic](http://micropython.org/static/doc/PYBv10b.pdf)).
A dab of hot-glue holds the switch in place on top of the processor.
Up until now, I've been using a [NetDuino Plus
2](http://netduino.com/netduinoplus2/specs.htm) which has the same processor
as the pyboard.
Now, when I want to flash a new version of MicroPython (which I do quite
frequently) I can press BOOT0 and RESET, and the board comes up in the DFU
bootloader.

