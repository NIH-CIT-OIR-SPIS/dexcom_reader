import constants
import datetime
import platform
import serial.tools.list_ports as port_list

def ReceiverTimeToTime(rtime):
  return constants.BASE_TIME + datetime.timedelta(seconds=rtime)

def find_usbserial():
  dexcom_port = ''
  if platform.system() == 'Windows':
    comports = port_list.comports()
    for i in range(0, len(comports)):
      print(i)
      if comports[i].manufacturer == 'Microsoft':
        dexcom_port = comports[i].device
    return dexcom_port
  else:
    raise NotImplementedError('Cannot find serial ports on %s'
                              % platform.system())
