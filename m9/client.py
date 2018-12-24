'''client program'''
from threading import Thread
import socket

'''reciver func for recieving responce from server '''
def receiver(server):
    data = b''
    while True:
        try:
            data = server.recv(1024)
        except:
            break
        if data:
            print('server response: '+str(data.decode()))
        else:
            break
    

host = '127.0.0.1'
port  = 5000
s = socket.socket()
s.connect((host, port))

'''func to take input from user '''
def main():
    message = input('-->')
    while message != 'x':
        s.send(message.encode())
        message = input()
    s.close()


if __name__ == '__main__':
    #main thread to take user input
    t= Thread(target=main)
    #thread to recive responce
    t2=Thread(target=receiver,args=(s,))
    t.start()
    t2.start()
    t.join()
    t2.join()
