import pyfirmata as pf
import time

port = 'COM3'

ard = pf.Arduino(port)

pin3 = ard.get_pin('d:3:p')
pin5 = ard.get_pin('d:5:p')
pin6 = ard.get_pin('d:6:p')
pin9 = ard.get_pin('d:9:p')
pin11 = ard.get_pin('d:11:p')

# print(dir(pin3))

while True:
    print('켜짐')
    pin3.write(50)
    pin5.write(50)
    pin6.write(50)
    pin9.write(50)
    pin11.write(50)
    time.sleep(1)
    
    print('꺼짐')
    pin3.write(0)
    pin5.write(0)
    pin6.write(0)
    pin9.write(0)
    pin11.write(0)
    time.sleep(1)