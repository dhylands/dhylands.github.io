---
layout: post
title: Bringing up MicroPython on the GHI Electronics G30TH
date: '2016-07-14T22:33:00.001-07:00'
author: Dave Hylands
tags:
- MicroPython
- STM32
modified_time: '2017-08-10T13:53:50.329-07:00'
thumbnail: https://4.bp.blogspot.com/-LJmeQSxX0Jc/V4hM50pr_qI/AAAAAAAAnbw/FWCA0hQOGN03AzBrx1bSZlVMtU8l6laNACKgB/s72-c/IMG_20160714_162633.jpg
blogger_id: tag:blogger.com,1999:blog-2189571833278528716.post-29581809831504611
blogger_orig_url: http://blog.davehylands.com/2016/07/bringing-up-micropython-on-ghi.html
---

I noticed that GHI Electronics makes a number of devices using the SM32F4
fmaily of processors, which also happens to be supported by MicroPython.

The G30TH caught my eye, which is basically a breakout board for the
STM32F401RET6 which has 512K of flash and 96K of RAM.


## Provide 3.3V

The board includes a USB connector, but doesn't include any onboard regulator,
so you'll need to provide 3.3V to power the board.

I happened to have a [Pololu 2842](https://www.pololu.com/product/2842) in my
drawer, so I decided to use that.

[![]({{ site.url}}/images/2016-07-14/image-0000.jpg)]({{ site.url}}/images/2016-07-14/image-0000.jpg)


Being paranoid, I put a piece of kapton tape over the bottom of the regulator
since it would be coming in contact with the metal housing on the USB
connector. The Kapton tape makes the white silkscreen look yellow in the photo
below:

[![]({{ site.url}}/images/2016-07-14/image-0001.jpg)]({{ site.url}}/images/2016-07-14/image-0001.jpg)


While I still had access, I soldered a piece of wire to the VIN signal on the
regulator, and then I soldered 2 header pins to the 3V3 and GND pins:

[![]({{ site.url}}/images/2016-07-14/image-0002.jpg)]({{ site.url}}/images/2016-07-14/image-0002.jpg)


VOUT on the regulator connects to 3V3 on the G30TH, and GND on the regulator
connects to GND on the G30TH. The red wire connects from VIN on the regulator
to V+ on the G30TH. V+ on the G30TH connects to VUSB on the USB connector.

[![]({{ site.url}}/images/2016-07-14/image-0003.jpg)]({{ site.url}}/images/2016-07-14/image-0003.jpg)


Now if you plug in the USB connector, both the PWR and USB LEDs should light.


## Build the firmware

You can grab the micropython source code using git:



    git clone https://github.com/micropython/micropython.git

and then install the G30TH board defintion into the tree:



    cd micropython/stmhal/boards
    git clone https://github.com/dhylands/G30TH.git
    cd ..

Finally, build the firmware (from within the micropyton/stmhal directory):



    make BOARD=G30TH



## Get the Board into DFU mode

I used a wire jumper to connect from 3V3 and pressed it on the B0 (BOOT0). I
used a female to female jumper wire with a single header pin plugged in one
end:

[![]({{ site.url}}/images/2016-07-14/image-0004.jpg)]({{ site.url}}/images/2016-07-14/image-0004.jpg)


I also used a short 6" USB cable to plug it into a USB extension cable. I
found plugging the 6" cable into the extension to be quite a bit easier than
plugging into the Micro B connector on the board. I could then hold the jumper
on B0 with one hand and plug the USB cable into the extension with the other
and get the board into DFU mode.

[![]({{ site.url}}/images/2016-07-14/image-0005.jpg)]({{ site.url}}/images/2016-07-14/image-0005.jpg)


With the board in DFU mode, **lsusb** should show an entry like this:



     Bus 001 Device 014: ID 0483:df11 STMicroelectronics STM Device in DFU Mode


and running dfu-util --list should report something like this:



    $ dfu-util --list
    dfu-util 0.8

    Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
    Copyright 2010-2014 Tormod Volden and Stefan Schmidt
    This program is Free Software and has ABSOLUTELY NO WARRANTY
    Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

    Found DFU: [0483:df11] ver=2200, devnum=14, cfg=1, intf=0, alt=3, name="@Device Feature/0xFFFF0000/01*004 e", serial="377A364D3234"
    Found DFU: [0483:df11] ver=2200, devnum=14, cfg=1, intf=0, alt=2, name="@OTP Memory /0x1FFF7800/01*512 e,01*016 e", serial="377A364D3234"
    Found DFU: [0483:df11] ver=2200, devnum=14, cfg=1, intf=0, alt=1, name="@Option Bytes  /0x1FFFC000/01*016 e", serial="377A364D3234"
    Found DFU: [0483:df11] ver=2200, devnum=14, cfg=1, intf=0, alt=0, name="@Internal Flash  /0x08000000/04*016Kg,01*064Kg,03*128Kg", serial="377A364D3234"



## Unprotect the device

The firmware on the G30TH is protected, so the first thing that needs to be is
to unprotect the device.

 **IMPORTANT: Once you unprotect the device (which will erase it) there's no
going back to the .NET firmware that came with it (since I don't believe that
firmware is distributed anywhere). So don't expect to "try" MicroPython and go
back to using .NET later.**

The device can be unprotected using dfu-util:



    dfu-util -s :unprotect:force -a 0 -d 0483:df11 -D build-G30TH/firmware.dfu

Note that DFU requires the -D option even though it won't be using the
firmware file. Unprotecting the device has the side effect of erasing it.



    $ dfu-util -s :unprotect:force -a 0 -d 0483:df11 -D build-G30TH/firmware.dfu
    dfu-util 0.8

    Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
    Copyright 2010-2014 Tormod Volden and Stefan Schmidt
    This program is Free Software and has ABSOLUTELY NO WARRANTY
    Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

    Deducing device DFU version from functional descriptor length
    Opening DFU capable USB device...
    ID 0483:df11
    Run-time device DFU version 011a
    Claiming USB DFU Interface...
    Setting Alternate Setting #0 ...
    Determining device status: state = dfuERROR, status = 10
    dfuERROR, clearing status
    Determining device status: state = dfuIDLE, status = 0
    dfuIDLE, continuing
    DFU mode device DFU version 011a
    Device returned transfer size 2048
    DfuSe interface name: "Internal Flash  "
    Device disconnects, erases flash and resets now


Unprotecting the device also resets the device, so you'll need to put it back
into DFU mode once more.


## Flash MicroPython

Now that the device is back in DFU mode once again, we can flash MicroPython:

```
make BOARD=G30TH deploy
```

If you've never flashed MicroPython before, there may be additional steps
required. The wiki page for [programming the STM32F4 Discovery
Board](https://github.com/micropython/micropython/wiki/Board-
STM32F407-Discovery#programming-from-linux-via-dfu) should have the
information required.

Once MicroPython has been programmed, then you can use your favorite terminal
program to open /dev/ttyACM0 and get a REPL: (I often use [usb-ser-
mon.py](https://github.com/dhylands/usb-ser-mon))



    $ usb-ser-mon.py
    Waiting for USB Serial Device ...
    USB Serial device with vendor 'MicroPython' serial '377A364D3234' connected @/dev/ttyACM0
    Use Control-X to exit.
    MicroPython v1.8.2-13-g08eac74 on 2016-07-14; G30TH with STM32F401CE
    Type "help()" for more information.
    >>>



