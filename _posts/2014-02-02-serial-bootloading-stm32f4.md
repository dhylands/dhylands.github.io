---
layout: post
title: Serial bootloading the STM32F4
date: '2014-02-02T10:37:00.000-08:00'
author: Dave Hylands
tags:
- STM32
modified_time: '2014-06-15T10:15:52.916-07:00'
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-9028248024102029363
blogger_orig_url: http://blog.davehylands.com/2014/02/serial-bootloading-stm32f4.html
---

I was helping out my [brother](http://blog.huvrobotics.com/) trying to figure out why
his [uCee board](http://blog.huvrobotics.com/2014/02/micropython-boards-crystal-
trouble.html) wasn't working. The STM32F4xx chips have an onboard bootloader
that can flash the chip using USB, CAN, or one of 2 UARTs.

The USB wasn't working (which was the planned interface to use), so I
suggested using one of the UARTs. The next trick was to find some code for
talking to the UART bootloader. I tried
[stm32ld](https://github.com/jsnyder/stm32ld) and jsnyder's
[stm32loader](https://github.com/jsnyder/stm32loader) and they would both
recognize the chip but then bailed when trying to unprotect.

I poked around a bit and came across this
[variant](https://github.com/espruino/Espruino/blob/master/scripts/stm32loader.py)
from the [Espruino project](https://www.espruino.com/). That version works on
my STM32F4DISCOVERY board and it worked on my brothers board.

The UART bootloader wants a raw .bin file without any special headers or
anything, so I used:



    arm-none-eabi-objcopy -O binary flash.elf flash.bin



to create a suitable binary file (flash.elf came from the
[MicroPython](https://micropython.org/) build).

To initiate the bootloader on the UART you need to make BOOT0 high, and then
press and release RESET (keep BOOT0 high while releasing RESET). Then run:



    ./stm32loader.py -p /dev/ttyUSB0 -evw flash.bin



Looking at the stm32loader.py code, it appears to support using DTR to reset
the processor, and RTS to control BOOT0. I haven't tested this out yet, but it
looks to be worth checking out.

