from socket import AF_INET,socket,SOCK_STREAM
import cv2
import numpy as np
import time

HOST =''
PORT = 33003
SIZE = (640, 360)
MSGLEN = 691200

def mysend(msg):
    totalsent = 0
    while totalsent < MSGLEN:
        print(totalsent)
        sent = client.send(msg[totalsent:])
        # if sent == 0:
        #     raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent
        # time.sleep(1)
    print(totalsent)

ADDR=(HOST,PORT)
SERVER=socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

SERVER.listen(1)
client, client_addr = SERVER.accept()

# img = cv2.imread("img/test1.png")
cam = cv2.VideoCapture(0)
ret, img = cam.read()

while(1):
    img = cv2.resize(img, SIZE)
    cv2.imshow("server", img)
    data = np.array(img)
    data = data.tostring()
    print(type(data))
    cv2.waitKey(1)
    mysend(data)
    ret, img = cam.read()

# client.send(data)
# print(len(data))


SERVER.close()