import usb

def list_usb():
  busses = usb.busses()
  for bus in busses:
    devices = bus.devices
    for dev in devices:
      print "Device: ", dev.filename
      print "  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor)
      print "  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct)

def read():
  print("Reading Sensor Data")

def get_acc():
  acc = 0.00
  return str(acc) + " m/s"

def get_rot():
  rot = 0.00
  return str(rot) + " d/s"

def get_alt():
  alt = 0.00
  return str(alt) + " m"

def get_gps():
  return 0
