# python version I used is: Python 3.8.5 

import socket
import threading

username = input("Choose your username: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

def receive():
    while True:
        try:

            message = client.recv(1024).decode('ascii')
            if message == ' ':
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:

            print("An error occured!")
            client.close()
            break
        
def write():
    while True:
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('ascii'))
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
