---
layout: post
title: OpenMVCam
date: '2014-10-15T22:18:00.000-07:00'
author: Dave Hylands
tags:
- MicroPython
- OpenMVCam
modified_time: '2014-10-15T22:18:21.359-07:00'
thumbnail: http://2.bp.blogspot.com/-GV6-2xcqnHU/VD9IUq5-TYI/AAAAAAAAZio/i7hqjFRKKb8/s72-c/IMG_20141015_210808.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-6272657987137926273
blogger_orig_url: http://blog.davehylands.com/2014/10/openmvcam.html
---

I signed up to get one of the early OpenMVCam boards, and mine arrived
yesterday.

One really cool thing is that it uses MicroPython to control it. Here's a
photo of the OpenMVCam board beside a MicroPython board (OpenMVCam on the
left), along with a photo of the back of the OpenMVCam board on the right. The
MicroPython board uses the 64-pin STM32F405, where the OpenMVCam board uses
the 100 pin STM32F407.




[![]({{ site.url }}/images/2014-10-15/image-0000.jpg)]({{ site.url}}/images/2014-10-15/image-0000.jpg)
[![]({{ site.url}}/images/2014-10-15/image-0001.jpg)]({{ site.url}}/images/2014-10-15/image-0001.jpg)


I decided to use the OpenMVCam to take a "selfie":


[![]({{ site.url }}/images/2014-10-15/image-0002.jpeg) ]({{ site.url
}}/images/2014-10-15/image-0002.jpeg)


This was taken in a mirror using the write-jpeg.py
python script, running on the openmv board to snap a photo. I need to figure
out how to focus the camera.

