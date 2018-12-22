'''Socket prog based on tcp for authorized attendance
client
 '''
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 6000        # The port used by the server

#tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


rollcall = input("Roll Number: ")
rollnum = "MARK-ATTENDANCE " + rollcall 
s.send(rollnum.encode())

#closes when correcly authorized
while True:
    message = s.recv(1024).decode()
    message_split = message.split(' ')
    print(message)
    if message_split[0] == 'SECRETQUESTION':
        answer = input('Enter the answer: ')
        s.send(("SECRETANSWER "+answer).encode())
    elif message_split[0] == "ATTENDANCE-SUCCESS":
        print("closing")
        break
    elif message_split[0] == "ATTENDANCE-FAILURE":
        s.send(rollnum.encode())
    #roll call not found
    else:
        rollcall = input("Roll Number: ")
        rollnum = "MARK-ATTENDANCE " + rollcall 
        s.send(rollnum.encode())
s.close()

