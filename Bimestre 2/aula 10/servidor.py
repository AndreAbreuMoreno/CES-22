import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
ip = '127.0.0.1'
port = 1234

clients = {}

s.bind((ip, port))
s.listen()
print('Server Ready...')
print('Ip Address of the Server::%s' % ip)


def handleClient(client, uname):
    clientConnected = True
    while clientConnected:
        msg = client.recv(1024).decode('ascii')
        for k, v in clients.items():
            v.send(msg.encode('ascii'))


while serverRunning:
    client, address = s.accept()
    uname = client.recv(1024).decode('ascii')
    print('%s connected to the server' % str(uname))


    if (client not in clients):
        clients[uname] = client
        threading.Thread(target=handleClient, args=(client, uname,)).start()