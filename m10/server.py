'''server program '''
import socket
import threading


s=socket.socket()
ip='127.0.0.1'
port=5000
clients=[]
s.bind((ip,port))
s.listen()
print("Server Ready......")
print("IP Address of the Server:%s"%ip)


'''func to send msgs to clients'''
def handleClient(client):
    while True:
        msg=client.recv(1024).decode()
        for c in clients:
            c.send(msg.encode())

'''main thread to handle client request '''
while True:
    client,addr=s.accept()
    print("%s connected to the server"%str(addr))
    client.send("Welcome to Messenger".encode())
    if (client not in clients):
        clients.append(client)
        threading.Thread(target=handleClient,args=(client,)).start()
