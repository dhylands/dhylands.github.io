---
layout: post
title: STM32CubeF4 gcc makefile example
date: '2014-03-11T08:45:00.001-07:00'
author: Dave Hylands
tags:
- STM32
- Software
modified_time: '2014-06-15T10:15:21.794-07:00'
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-5222389780184891770
blogger_orig_url: http://blog.davehylands.com/2014/03/stm32cubef4-gcc-makefile-example.html
---

I started to play with the [STM32CubeF4
hal](http://www.st.com/web/en/catalog/tools/PF259243#) code, in the context of
helping to add support for it in MicroPython. I looked around for an example
Makefile which used gcc, and couldn't find one.
So, of course, I created my own.
You can find my Makefile (if you've seen MicroPython's makefile then this will
look familiar, since I copied most of the bits and pieces from there)
[here](https://github.com/dhylands/stm32cubef4-gpio-exti). It's setup to work
with the STM32F4-Discovery board.
The STM32F407VG_FLASH.ld and startup_stm32f407xx.s came from the TrueSTUDIO
tree.
The Makefile only works for the GPIO_EXTI example and would need to be
modified for other examples. I'll probably only do the one example, since
that's enough to get the basics working.




