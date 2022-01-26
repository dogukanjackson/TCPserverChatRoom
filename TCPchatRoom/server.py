# 230201071
# python version I used is: Python 3.8.5 

import socket
import threading

host = '127.0.0.1'
port = 12345


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
usernames = []

def release(message):
    for client in clients:
        client.send(message)
        
        
def manage(client):
    while True:
        try:

            message = client.recv(1024)
            release(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            release('{} left!'.format(username).encode('ascii'))
            usernames.remove(username)
            break
        
def receive():
    while True:
        client, address = server.accept()
        print("Connected with the addres:",str(address))

        client.send(' '.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        print("User connected with the username: {}".format(username))
        release(f'{username} has been joined to the server!'.encode('ascii'))
        client.send('\nConnected to server!'.encode('ascii'))

        thread = threading.Thread(target=manage, args=(client,))
        thread.start()
        
        
receive()
