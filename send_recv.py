from socket import AF_INET,socket,SOCK_STREAM

def send(client, msg, MSGLEN = 691200):
    totalsent = 0
    while totalsent < MSGLEN:
        # print(totalsent)
        sent = client.send(msg[totalsent:])
        # if sent == 0:
        #     raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent
        # time.sleep(1)
    # print(totalsent)

def receive(client_socket, MSGLEN = 691200):
    msg = b''
    while len(msg) < MSGLEN:
        chunk = client_socket.recv(MSGLEN-len(msg))
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        msg = msg + chunk
    return msg