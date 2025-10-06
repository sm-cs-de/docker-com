import usb.core
import usb.util

dev = usb.core.find()
if dev is None:
    print("No USB device found")
else:
    print(f"Found USB device: {hex(dev.idVendor)}:{hex(dev.idProduct)}")

