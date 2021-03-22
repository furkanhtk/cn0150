import time
import spidev

current_time = time.localtime()

#f = open("oscilog.txt", "w")


bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)
#spi.max_speed_hz = 500000
spi.mode = 0

#msg = [0b00000000,0b00000001,0b00000010,0b00000011]
msg = [0x01]

while True:
   
  time.sleep(0.5)
  #reply = spi.xfer(msg)
  spi.writebytes(msg)
  reply = spi.readbytes(2)
  print(reply)
  #list  = spi.readbytes(2)
  result = reply[0] << 8 | reply[1]
  print("Result = {}-----{}".format(result,reply))
  current_time = time.localtime()
