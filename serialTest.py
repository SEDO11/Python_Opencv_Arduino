import serial
import time

port = 'COM3'
rate = 9600

# 아두이노 ide를 켜놓은 상태에서는 에러남
ard = serial.Serial(port, rate) 
# print(type(ard)) # 타입 확인
# print(dir(ard)) # 함수 확인

# 아두이노와 소통하기 위해 incode 
# str -> bytes
s = b'hello'
# print('s', type(s))

# bytes -> str
# c = b'world'
# c = c.decode('utf-8')
# print('c', type(c))

while True:
    command = input('아두이노 명령어:')
    ard.write(command.encode())
    time.sleep(0.1)
    
    if ard.readable():
        response = ard.readline()
        print(response[:len(response)-1].decode())