from socket import AF_INET,socket,SOCK_STREAM
import cv2
import numpy as np
import time
from send_recv import *

HOST =''
PORT = 33003
SIZE = (640, 360)
MSGLEN = 691200

ADDR=(HOST,PORT)
SERVER=socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

SERVER.listen(1)
client, client_addr = SERVER.accept()

while(1):
	data = receive(client)
	new = np.frombuffer(data, dtype=np.uint8).reshape((360, 640, 3))
	
	############## process frames here ##############
	
	tosend = new.tostring()
	send(client, tosend)

SERVER.close()