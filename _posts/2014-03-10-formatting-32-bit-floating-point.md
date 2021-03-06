---
layout: post
title: Formatting 32-bit floating point numbers (aka convert 32-bit float to string)
date: '2014-03-10T08:30:00.000-07:00'
author: Dave Hylands
tags:
- MicroPython
- Software
modified_time: '2014-06-15T10:14:51.568-07:00'
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-5545807640079864856
blogger_orig_url: http://blog.davehylands.com/2014/03/formatting-32-bit-floating-point.html
---

While working on MicroPython, I went looking for some code to format 32-bit
floating point numbers.
I spent quite a while looking, and all of the examples I found were focused on
doubles or long-doubles and used a lot more RAM than what was required for
just 32-bit floats.
Of the ones, I did find, Fred Bayer's
[pdouble.c](https://tangentsoft.net/palmfaq/src/pdouble.c) was one of the
easiest to understand.
I used that as a base, and added support for e, f, and g formats, as well as
allowing the caller to specify the buffer (and size) to receive the results.
This version uses no RAM (other than some stack). The caller provides the
output buffer, and all globals are constant so that they can come from flash.
All of the arithmetic is either 32-bit integer or 32-bit float, so that
processors like the Cortex-M4's with FPU can use this with no extra support
libraries.
I figured that others might find it useful, so I put my version, along with
some test code in [github](https://github.com/dhylands/format-float).
Since Fred Bayer's code (on which this code was based) was pubic domain, I
made my code public domain. So you can use it however you like. If you do use
it, it would be nice to hear from you, but even that's not a requirement.

