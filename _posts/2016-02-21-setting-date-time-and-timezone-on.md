---
layout: post
title: Setting the date, time, and timezone on the Raise3D N2
date: '2016-02-21T00:00:00.001-08:00'
author: Dave Hylands
tags:
- Raise3D
modified_time: '2016-05-25T16:37:20.680-07:00'
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-4800085514134521721
blogger_orig_url: http://blog.davehylands.com/2016/02/setting-date-time-and-timezone-on.html
---

UPDATE: It turns out that later versions of the firmware now have the ability
to set the timezone, date and time. I currently have version 0.6.5.3247
installed. To change the timezone, click on the little gear icon in the upper
right corner, which will bring up "Settings". Then chose the "Other" category
and finally, "Date & Time". You need to press on the > over on the right hand
side.

Touch the > over on the right of the Timezone line, and then in the search box
start typing the name of your time zone city. You can find a list of time zone
cities [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
(note that this list has the timezone name shown first).

I start to type van and then clicked on "Vancouver, Pacific". Once entered,
then press the back < and then enter the date and time.

Restart (either by using Settings -> Machine -> Restart, or by power cycling)
and your timezone and date/time should be correct.



The following is the original blog post, which I'm keeping for reference.

This is a bit technical. If I glossed over something, feel free to ask
questions. Hopefully the good folks at Raise3D will fix their firmware to
allow the date/time/timezone information to be entered.

I noticed when printing files from the sdcard or MMC card, that the time was
being reported in UTC, and that the timestamp on internal files was from 2015.

Since you can ssh into the root account on the printer, I decided to see if I
could correct this. The printer uses busybox, but it appears to be using glibc
rather than uclibc.

With glibc, you can set the default timezone by making /etc/localtime be a
special timezone file or a symlink to a special timezone file.

I run Ubuntu on my desktop, and it had an /etc/localtime which was a file (not
a symlink). It mostly contains binary data (if you do a hex dump you'll see
your timezone strings buried in there). For convenience, I put a copy of the
/usr/share/zoneinfo directory tree in my [github
account](https://github.com/dhylands/tzdata/tree/master/zoneinfo). Many of the
files are symlinks. For example, I normally use America/Vancouver as my
timezone, and if I find that file, it shows ../Canada/Pacifc and
../Canada/Pacific is not a symlink, but a real file. So I downloaded the
Canada/Pacific timezone file to use as my timezone file.

First thing to do is to verify your current timezone:



    ssh root@192.168.0.158
    date


replace 192.168.0.158 with the IP address of your printer. In my case it
showed UTC as the timezone and a year of 2015.

I entered Control-D to quit from the ssh sesseion and then copied the
Canada/Pacific file from my github repository (download the raw file) to the
/etc/localtime file on my printer:



    scp Pacific root@192.168.0.158:/etc/localtime


Now restart the printer. If you now ssh into the printer then the date command
should show the correct timezone, but will still show the incorrect time. You
can correct the time by ssh'ing back into the printer and using the date
command. To set the date, you need to call date with a bunch of numbers in the
format MMDDhhmmYYYY where MM is the 2 digit month, DD is the 2 digit date, hh
is the 2 hour time (in 24 hour format), mm is the minute, and YYYY is the 4
digit year. For example:



    186 >ssh root@192.168.0.158
    root@raise3d:~# date 022023562016
    Sat Feb 20 23:56:00 PST 2016




