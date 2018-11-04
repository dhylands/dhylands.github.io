---
layout: post
title: USB Serial Monitor
date: '2014-01-31T16:28:00.000-08:00'
author: Dave Hylands
tags:
- Python
modified_time: '2014-06-15T10:16:14.656-07:00'
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-5048586196121051252
blogger_orig_url: http://blog.davehylands.com/2014/01/usb-serial-monitor.html
---

Lately, I've been working with USB Serial devices, and I've discovered that
many serial programs don't like it when the serial device is disconnected.

So I decided to write my own little monitor program in python. It hooks into
pyudev to get the add/remove notifications when usb devices are plugged in or
removed (so currently it only works under linux).

Source code can be found [here](https://github.com/dhylands/usb-ser-mon). It
requires pyudev version 0.16 or newer.

If you run:



    ./usb-ser-mon.py -l

it will show you the currently connected devices.




    USB Serial Device with vendor 'Teensyduino' serial '21973' found @/dev/ttyACM1
    USB Serial Device with vendor 'Prolific_Technology_Inc.' found @/dev/ttyUSB0
    USB Serial Device with vendor 'STMicroelectronics' serial '00000000050C' found @/dev/ttyACM0


If you want to connect with the STM device (an STM32FDISCOVERY board in this
situation), then you might do:




    1247 >./usb-ser-mon.py -n Teensy
    USB Serial device with vendor 'Teensyduino' serial '21973' connected @/dev/ttyACM1

    >>>

In the previous example the Teensy was already connected. If I unplug and
replug the Teensy device then I'd see:





    USB Serial device @ /dev/ttyACM1  disconnected.

    Waiting for USB Serial Device with vendor 'Teensy' ...
    USB Serial device with vendor 'Teensyduino' serial '21973' connected @/dev/ttyACM1
    Done executing '/src/main.py'
    Micro Python for Teensy 3.1
    Type "help()" for more information.
    >>>

You only need to use as many characters as are required to uniquely identify a
device, so I could use:



    ./usb-ser-mon.py -n STM

to connect to the Discovery board.

