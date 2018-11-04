---
layout: post
title: STM32CubeF4 gcc makefile example for FreeRTOS
date: '2016-10-04T11:27:00.000-07:00'
author: Dave Hylands
tags:
- STM32
modified_time: '2016-10-04T11:27:24.415-07:00'
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-6347735780477404867
blogger_orig_url: http://blog.davehylands.com/2016/10/stm32cubef4-gcc-makefile-example-for.html
---

Following along from my earlier blog post
[STM32CubeF4 gcc makefile example]({% post_url 2014-03-11-stm32cubef4-gcc-makefile-example %}),
I modified the Makefile to work with one of the FreeRTOS
examples included in the STM32CubeF4 (v1.13.0). This particular example
flashes some LEDs on the STM32F469 Discovery board. The biggest wrinkle I ran
into was having to add an _exit function. I grabbed a syscalls.c from
elsewhere in the STM32CubeF4 tree and #if 0'd out some timezone functions
which were failing to compile. You can find my repository with the Makefile,
syscalls.c and instructions
[here](https://github.com/dhylands/stm32cubef4-freertos).

