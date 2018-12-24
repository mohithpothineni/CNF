'''client program '''
import socket
import threading

s=socket.socket()
port=5000
username=input("Enter user name:")
ip="127.0.0.1"
s.connect((ip,port))


'''func to handle responce'''
def receiveMsg(sock):
    while True:
        msg=sock.recv(1024).decode()
        print(msg)

'''thread for receiving messages'''
threading.Thread(target=receiveMsg,args=(s,)).start()

'''main thread handles user input'''
while True:
    tempMsg=input("")
    msg=username+'>>'+tempMsg
    s.send(msg.encode())
