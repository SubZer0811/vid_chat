from socket import AF_INET, socket, SOCK_STREAM
import cv2
import numpy as np
from send_recv import *

HOST=''
PORT=33003
SIZE = (640, 360)
MSGLEN = 691200

ADDR=(HOST,int(PORT))
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)

cam = cv2.VideoCapture(0)
ret, img = cam.read()

while(1):
	img = cv2.resize(img, SIZE)
	data = np.array(img)
	data = data.tostring()
	send(client_socket, data)

	# receiving processed frames from server
	recvd = receive(client_socket)
	recvd = np.frombuffer(recvd, dtype=np.uint8).reshape((360, 640, 3))
	cv2.imshow("vid_chat", recvd)

	key = cv2.waitKey(1)
	if key == ord('q'):
		break
	
	ret, img = cam.read()

client_socket.close()