dev-mapper
==========

The dev-mapper is converter which the sys-pci-address to the device file.  
The Serial device in the linux changed according it makes device file name  
whenever plugged in order. Sometimes this makes it hard.

The USB Port physically has a PCI address.  
In my raspberry-pi, the serial device, /dev/ttyUSB0 has been pluged a specific USB port in.

This port has a PCI address like as:  

    /sys/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.2/1-1.2:1.0

Even if you reboot your computer or connect a new serial device, this PCI address does not change.  However, sometimes it can be changed if only the kernel is updated.


### How to know the PCI address of the serial device ?

Run command as follow:  

    #> find /sys -name ttyUSB0
    /sys/bus/usb-serial/devices/ttyUSB0
    /sys/bus/usb-serial/drivers/cp210x/ttyUSB0
    find: `/sys/devices/platform/soc/3f200000.gpio/gpio/gpiochip0': Permission denied
    /sys/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.2/1-1.2:1.0/ttyUSB0
    /sys/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.2/1-1.2:1.0/ttyUSB0/tty/ttyUSB0
    /sys/class/tty/ttyUSB0
    find: `/sys/class/gpio': Permission denied
    find: `/sys/kernel/debug': Permission denied


### Install

    #> pip install -U dev-mapper


### Usage

    #> python -m devmapper.devmap serial  /sys/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.2/1-1.2:1.0
    /dev/ttyUSB0
