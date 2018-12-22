'''Socket prog based on tcp for authorized attendance
Server
 '''

import socket
import threading

'''file reading and generation of dict '''
f = open('data.csv')
raw_data = f.read()
f.close()

data = {}
raw_data_split = raw_data.split("\n")
raw_data_split.pop()

for line in raw_data_split:
    line_data = line.split(",")
    data[line_data[0]] = [line_data[1],line_data[2]]

'''socket generation'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 6000
serverRunning = True
s.bind((ip, port))
s.listen()
number = -1

'''authorization and responce to clients '''
def authorizing(client):
    clientConnected = True
    rollcall_given  = 0
    while clientConnected:
        message = client.recv(1024).decode()
        message_split = message.split(" ")
        if message_split[0] == "MARK-ATTENDANCE":
            if data.get(message_split[1]) is not None:
                client.send(("SECRETQUESTION "+data[message_split[1]][0]).encode())
                rollcall_given = message_split[1]
            else:
                client.send(b"ROLLNUMBER-NOTFOUND")
        elif message_split[0] == "SECRETANSWER":
            if message_split[1] == data[rollcall_given][1]:
                client.send(b"ATTENDANCE-SUCCESS")
                clientConnected = False
            else:
                client.send(b"ATTENDANCE-FAILURE")
    client.close()




'''loop listening for clinets '''
print("Server is running, waiting for connections.")
while serverRunning:
    client, address = s.accept()
    threading.Thread(target = authorizing, args = (client, )).start()
