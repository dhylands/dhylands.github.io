---
layout: post
title: "Capturing USB Serial data using wireshark"
tags:
- wireshark
- "USB Serial"
---

While working with a ConBee USB dongle for talking to Zigbee devices, I
wanted to examime the serial stream being sent to/from the deConz
program. This describes the steps I took to capture and examine the
serial stream.

The steps described here were done using a linux computer running
Ubuntu 18.04.

## Allow wireshark to access usbmon.

When you install wireshark, you're presented with a dialog asking if
non-superusers should be able to capture packets. Unfortunatly,
this only applies to the regular networking interfaces and doesn't
apply to usbmon.

You can verify that you are a member of the wireshark group by using
the `id` command. The output of the id command will include all of the
groups that your user is a member of. Note that group membership is
inherited by sub-processes, so if you change your group membership, then
you'll need to logout and log back in to have the change take effect.

I created a file called `/etc/udev/rules.d/99-usbmon.rules`
```
# Allows members of the wireshark group to access the usbmon device
SUBSYSTEM=="usbmon", GROUP="wireshark", MODE="0640"
```
and then ran:
```
sudo udevadm control --reload-rules
sudo udevadm trigger
```
This causes the `/dev/usbmon*` files to have a group of `wireshark`,
rather than a group of `root`, and if your user is a member of the
`wireshark` group, then you'll be able to access the `/dev/usbmon*`
files without being the root user.

## Load usbmon.

Use the command:
```
sudo modprobe usbmon
```
to load the usbmon module. This is required to allow wireshark
to intercept usb traffic.

Verify that the permissions are correct. You should see that the device
nodes in /dev/usbmon have a group of wireshark:
```
$ ls -l /dev/usbmon*
crw-r----- 1 root wireshark 240, 0 Nov  7 13:43 /dev/usbmon0
crw-r----- 1 root wireshark 240, 1 Nov  7 13:43 /dev/usbmon1
crw-r----- 1 root wireshark 240, 2 Nov  7 13:43 /dev/usbmon2
...
```

## Determine which bus and device your usb serial device is on.

Determine which of the usbmon devices to use by looking at the output
of the `lsusb` command.
I was usisg a ConBee which had VID:PID of 0403:6015, so one of the
lines of my lsusb output looked like this:
```
Bus 005 Device 003: ID 0403:6015 Future Technology Devices International, Ltd Bridge(I2C/SPI/UART/FIFO)
```
The number 005 after the word `Bus` tells us that you should use usbmon5.
Also make note of the 003 after the word `Device`. We'll use those later.

## Capture your data.

Start wireshark capture on usbmon5 (replace the 5 the bus number
determined above).

Start using your serial device. Once you've finished capturing your data
you can reduce the amount of data using a display filter (unfortunately
wireshark doesn't support capture filters with usbmon). I use something
like the following, replacing the bus and device numbers as determined
above:

```
usb.bus_id == 5 && usb.device_address == 3 && usb.capdata
```

Export the data using: File->Export Packet Dissections->As JSON...
choosing "All Packets" and "Displayed".

This will generate a JSON file containing all of the received and
sent data.

The following example script will then print the read/write streams.

```javascript
#!/usr/bin/env node

'use strict';

// Since this is just an example, we'll just read the entire JSON
// file in.
const json = require('./deconz-zcl.json');

const isFTDI = true;

for (const packet of json) {
  const layer = packet._source.layers;
  const frameNum = layer.frame['frame.number'];
  const timeStamp = layer.frame['frame.time_relative'].slice(0, -6);
  const usb = layer.usb;
  let data = layer['usb.capdata'].replace(/:/g, '');

  const read = usb['usb.dst'] === 'host';
  if (read) {
    if (isFTDI) {
      // Remove the FTDI status bytes
      data = data.slice(4);
    }
    if (data.length == 0) {
      continue;
    }
  }

  let label = `     ${timeStamp}`.slice(-9);
  label += `     ${frameNum}`.slice(-6);
  label += read ? ' R:' : ' W:';

  console.log(label, Buffer.from(data, 'hex'));
}
```
Note that `isFTDI` should be set to true if you're using an FTDI based
adapter since the FTDI inserts 2 status bytes at the beginning of each
data frame.

Here's some sample output:
```
    6.806   877 W: <Buffer c0 07 00 00 08 00 00 00 00 f1 ff c0>
    6.825   883 R: <Buffer c0 07 00 00 08 00 aa 00 0b 3c ff c0>
    6.828   885 W: <Buffer c0 0d 01 00 09 00 00 00 00 00 e9 ff c0>
    6.841   889 R: <Buffer c0 0d 01 00 09 00 00 05 0b 26 b3 ff c0>
    6.844   891 W: <Buffer c0 11 02 00 0b 00 04 00 11 93 c8 00 72 fe c0>
    6.857   895 R: <Buffer c0 11 02 00 0b 00 04 00 11 00 c8>
    6.873   899 R: <Buffer 00 05 ff c0>
```
