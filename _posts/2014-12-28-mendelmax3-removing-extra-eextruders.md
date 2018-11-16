---
layout: post
title: MendelMax3 - Removing extra extruders from GLCD
date: '2014-12-28T00:00:00.000-08:00'
author: Dave Hylands
tags:
- MM3
modified_time: '2014-12-28T01:45:56.465-08:00'
thumbnail: http://1.bp.blogspot.com/-knzYtiHEoWo/VJ-jccLmUII/AAAAAAAAb_M/DkZCNHx8cmc/s72-c/status_screen0_115x19.png
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-2660604630039872596
blogger_orig_url: http://blog.davehylands.com/2014/12/mendelmax3-removing-extra-eextruders.html
---

By default the GLCD display always shows 3 extruders, even when you only have
one or two installed.

This blog post will show you how to modify your firmware to only display the
number of extruders that you have configured.

The MendelMax3 uses a [RAMBo](https://ultimachine.com/content/rambo-13) board,
which runs Marlin firmware. I created a github repository containing the
initial firmware image I got from [MakersToolWorks
(MTW)](https://makerstoolworks.com/). The master branch of my
[repo](https://github.com/dhylands/MM3-Firmware/) contains the original code I
got from MTW. The [test
branch](https://github.com/dhylands/MM3-Firmware/tree/test) contains my
changes.

After poking around for  a bit, I determined that the
[lcd_implementation_status_screen](https://github.com/dhylands/MM3-Firmware/blob/master/MTW_Marlin/Marlin/dogm_lcd_implementation.h#L158-L326)
routine draws the main status screen. The extruders appeared to be drawn as
part of [these two lines of
code](https://github.com/dhylands/MM3-Firmware/blob/master/MTW_Marlin/Marlin/dogm_lcd_implementation.h#L166-L167)
which basically draws a bitmap.

The bitmaps are contained in the
[DOGMbitmaps.h](https://github.com/dhylands/MM3-Firmware/blob/master/MTW_Marlin/Marlin/DOGMbitmaps.h)
file.

To clarify what I was seeing, I whipped up a quick and dirty python script to
convert the monochrome bitmap into a raw RGB image.



    #!/usr/bin/python -u

    """Program which converts an ASCII test into raw binary"""

    from __future__ import print_function
    import argparse
    import os
    import sys

    def main():
        parser = argparse.ArgumentParser(
            prog="txt2raw.py",
            usage="%(prog)s text-file",
            description="Convert a text file of ASCII hex into raw binary"
        )
        parser.add_argument(
            dest="txt_filename",
            help="Name of text file"
        )
        args = parser.parse_args(sys.argv[1:])
        raw_root, raw_ext = os.path.splitext(args.txt_filename)
        raw_filename = raw_root + ".data"

        print("txt_filename =", args.txt_filename)
        print("raw_filename =", raw_filename)

        with open(args.txt_filename, 'rb') as txt_f:
            with open(raw_filename, 'wb') as raw_f:
                for line in txt_f:
                    line = line.rstrip()
                    for val in line.split(','):
                        if val:
                            num = int(val, 0)
                            for i in range(8):
                                if num & (1 << (7 - i)):
                                    raw_f.write(b'\x00\x00\x00')
                                else:
                                    raw_f.write(b'\xff\xff\xff')

    main()



Running this on status_screen0_bmp yielded a raw RGB file, which I opened in
gimp and set the width to 120, and height to 19 giving:

[![]({{ site.url }}/images/2014-12-28/image-0000.png)]({{ site.url}}/images/2014-12-28/image-0000.png)

and status_screen1_bmp showed:

[![]({{ site.url }}/images/2014-12-28/image-0001.png)]({{ site.url}}/images/2014-12-28/image-0001.png)


which are the 2 bitmaps used to animate the cooling fans. Getting rid of the
extra extruders means that the bitmap will need to be modified.

Looking at the ASCII data:



    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7F,0xFF,0xE0,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x70,0x00,0xE0,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x63,0x0C,0x60,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x47,0x0E,0x20,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x4F,0x0F,0x20,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x5F,0x0F,0xA0,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x5E,0x07,0xA0,
    0x7F,0x80,0x00,0x3F,0xC0,0x00,0x3F,0xC0,0x00,0x41,0x04,0x00,0x40,0x60,0x20,
    0xFB,0xC0,0x00,0x79,0xE0,0x00,0x79,0xE0,0x00,0x20,0x82,0x00,0x40,0xF0,0x20,
    0xF3,0xC0,0x00,0x76,0xE0,0x00,0x76,0xE0,0x00,0x20,0x82,0x00,0x40,0xF0,0x20,
    0xEB,0xC0,0x00,0x7E,0xE0,0x00,0x7E,0xE0,0x00,0x41,0x04,0x00,0x40,0x60,0x20,
    0x7B,0x80,0x00,0x3D,0xC0,0x00,0x39,0xC0,0x00,0x82,0x08,0x00,0x5E,0x07,0xA0,
    0x7B,0x80,0x00,0x3B,0xC0,0x00,0x3E,0xC0,0x01,0x04,0x10,0x00,0x5F,0x0F,0xA0,
    0xFB,0xC0,0x00,0x77,0xE0,0x00,0x76,0xE0,0x01,0x04,0x10,0x00,0x4F,0x0F,0x20,
    0xFB,0xC0,0x00,0x70,0xE0,0x00,0x79,0xE0,0x00,0x82,0x08,0x00,0x47,0x0E,0x20,
    0xFF,0xC0,0x00,0x7F,0xE0,0x00,0x7F,0xE0,0x00,0x41,0x04,0x00,0x63,0x0C,0x60,
    0x3F,0x00,0x00,0x1F,0x80,0x00,0x1F,0x80,0x00,0x00,0x00,0x00,0x70,0x00,0xE0,
    0x1E,0x00,0x00,0x0F,0x00,0x00,0x0F,0x00,0x01,0xFF,0xFF,0x80,0x7F,0xFF,0xE0,
    0x0C,0x00,0x00,0x06,0x00,0x00,0x06,0x00,0x01,0xFF,0xFF,0x80,0x00,0x00,0x00

The numbers highlighted in red is the bitmap data for the #3 extruder. You can
see similar columns of numbers to the left for extruders #1 and #2. Replacing
the red numbers with 0x00 will make the extruder disappear.

So I copied and pasted the data and added:



    #if EXTRUDERS > 2
    ...include original bitmaps...
    #elif EXTRUDERS > 1
    ...include modified bitmap with extruder 3 blanked out...
    #else
    ...include modified bitmap with extruders 2 & 3 blanked out...
    #endif

You can find these changes
[here](https://github.com/dhylands/MM3-Firmware/blob/test/MTW_Marlin/Marlin/DOGMbitmaps.h#L80-L236).Later
on in the lcd_implementation_status_screen routine, it prints a line of 3
dashes underneath the extruder, and since we no longer have the extruders, I
commented the code that prints the dashes out
[here](https://github.com/dhylands/MM3-Firmware/blob/test/MTW_Marlin/Marlin/dogm_lcd_implementation.h#L235-L237)
and
[here](https://github.com/dhylands/MM3-Firmware/blob/test/MTW_Marlin/Marlin/dogm_lcd_implementation.h#L256-L258).

For my configuration, EXTRUDERS is set to 2, and now my GLCD screen looks like
this:

[![]({{ site.url }}/images/2014-12-28/image-0002.jpg)]({{ site.url}}/images/2014-12-28/image-0002.jpg)


I changed the "MendelMax2" to "Dave's MM3" by changing
[language.h](https://github.com/dhylands/MM3-Firmware/blob/test/MTW_Marlin/Marlin/language.h#L36-L37)

