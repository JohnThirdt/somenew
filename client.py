import socket
import json


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    s.sendto(input().encode(), ('192.168.202.255', 10000))
