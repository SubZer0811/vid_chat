from socket import AF_INET, socket, SOCK_STREAM
import cv2
import numpy as np

HOST=''
PORT=33003
SIZE = (360, 640, 3)
MSGLEN = 691200

def myreceive():
    msg = b''
    while len(msg) < MSGLEN:
        chunk = client_socket.recv(MSGLEN-len(msg))
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        msg = msg + chunk
    return msg

ADDR=(HOST,int(PORT))
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)

# data = client_socket.recv(691200)

while(1):
    data = myreceive()
    print(len(data))
    new = np.frombuffer(data, dtype=np.uint8).reshape((360, 640, 3))
    cv2.imshow("testing", new)
    cv2.waitKey(1)

cv2.waitKey(0)
client_socket.close()