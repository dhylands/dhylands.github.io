---
layout: post
title: Raise3D N2 Printer - Unpacking and First Print
date: '2016-02-16T22:27:00.000-08:00'
author: Dave Hylands
tags:
- Raise3D
modified_time: '2016-02-17T06:44:49.040-08:00'
thumbnail: https://4.bp.blogspot.com/-stXxmcaNKT4/VsPuwiQlD7I/AAAAAAAAkxk/hMnPrj6QYIM/s72-c/IMG_20160205_141544.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-1150028167471048524
blogger_orig_url: http://blog.davehylands.com/2016/02/raise3d-n2-printer-unpacking-and-first.html
---

I ordered a [Raise3D N2](http://www.raise3d.com/products/n2-pre-order) printer
as part of a [KickStarter](https://www.kickstarter.com/projects/raise3d
/raise3d-raise-the-standard-of-3d-printing) campaign. All of the Canadian
orders were container shipped to the good folks at
[filaments.ca](http://filaments.ca/) and then shipped out to individuals.



Mine finally arrived. Wow, that's a huge box (about 28" x 29" x 32").



[![]({{ site.url}}/images/2016-02-16/image-0000.jpg)]({{ site.url}}/images/2016-02-16/image-0000.jpg)


It was fairly easy to unpack. My outside door is 36" so it came in through
that easily, but with the cardboard cap and bottom on, it wouldn't quite fit
through a 30" door opening (at least not without removing the door), so I
unboxed it in the hallway and then moved it. The printer was very well packed,
and the cardboard only had minor gouges and scratches on the bottom.


[![]({{ site.url}}/images/2016-02-16/image-0001.jpg)]({{ site.url}}/images/2016-02-16/image-0001.jpg)


The buildplate was covered in BuildTak, but they didn't do a very good job
applying it. Mine had at least a dozen bubbles on it. I used a rounded piece
of plastic to smooth out the bubble and pricked each one with a pin to allow
the air to escape.This photo was taken from the back (glass side).


[![]({{ site.url}}/images/2016-02-16/image-0002.jpg)]({{ site.url}}/images/2016-02-16/image-0002.jpg)


Here's a photo from the BuildTak side before I removed the bubbles. It
probably took me half an hour or so to remove all of the bubbles.


[![]({{ site.url}}/images/2016-02-16/image-0003.jpg)]({{ site.url}}/images/2016-02-16/image-0003.jpg)


IdeaMaker (Raise3D's slicing software) is currently only available for Windows
and Mac (they claim that a Linux version is forthcoming - I hope). I had to
install windows on one of my laptops so I could run IdeaMaker. I tried running
in a VM, but it immedialtely crashed. As far as I can tell, you can use any
slicing software you like, so you should be able to use other slicers as well.

Here's a video of my very first print. I normally don't print a raft, but it
seems to have added one. I expect that this is just a setting in the software
someplace. I decided to do a Marvin as my first print. I made no adjustments
to the printer before printing this. I upgraded to the dual extruder option,
and my printer came with one spool of red PLA and one spool of yellow PLA. I
printed the Marvin using the red PLA.



The printer comes with a builtin touch screen. Here's a shot while it was part
way through printing.


[![]({{ site.url}}/images/2016-02-16/image-0004.jpg)]({{ site.url}}/images/2016-02-16/image-0004.jpg)


The windows software can connect to the printer over the network and upload
files to internal storage. It turns out you can ssh into the printer too. The
printer contains a processor running linux to manage the network and touch
screen, and also has a processor for doing the realtime control.
Unfortunately, the root account on the linux side of things has no password
(which is bad). If you set a root password, then the windows software will no
longer connect remotely to the printer. Hopefully, they'll add an option to
use passwordless ssh login so that I can set a root password.

Here's a shot while printing.


[![]({{ site.url}}/images/2016-02-16/image-0005.jpg)]({{ site.url}}/images/2016-02-16/image-0005.jpg)


The build platform has 2 leadscrews, one on the middle of each side.


[![]({{ site.url}}/images/2016-02-16/image-0006.jpg)]({{ site.url}}/images/2016-02-16/image-0006.jpg)


A shot through the front door, while printing.


[![]({{ site.url}}/images/2016-02-16/image-0007.jpg)]({{ site.url}}/images/2016-02-16/image-0007.jpg)


The finished print. I let the build plate cool down to about 29C and was able
to remove the Marvin by hand. This was sliced using medium settings (0.15mm
layer height) in the IdeaMaker software.


[![]({{ site.url}}/images/2016-02-16/image-0008.jpg)]({{ site.url}}/images/2016-02-16/image-0008.jpg)


A shot of the teeny tiny Marvin in the middle of the build plate (you can
supposedly print 12" x 12" x 12").


[![]({{ site.url}}/images/2016-02-16/image-0009.jpg)]({{ site.url}}/images/2016-02-16/image-0009.jpg)


Marvin removed from the build plate. I was able to remove the Marvin from the
raft by hand.


[![]({{ site.url}}/images/2016-02-16/image-0010.jpg)]({{ site.url}}/images/2016-02-16/image-0010.jpg)


The filament cooling could definitely be improved. There were some droops on
the back due to insufficient cooling. Fortunately, it looks like it will be
possible to wire in an additional fan or 2. I recommend signing up for the
[Raise 3D Mailing
List](https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!forum/raise3d).
There have already been several mods posted.


[![]({{ site.url}}/images/2016-02-16/image-0011.jpg)]({{ site.url}}/images/2016-02-16/image-0011.jpg)


That's all for now. I look forward to using this more.

