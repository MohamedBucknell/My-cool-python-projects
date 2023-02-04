
import threading
import socket

host = '127.0.0.1' #local host
port = 55555 # any port shall do the task
#sock stream indicates the stream is tcp type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
# listens for incoming connections
server.listen()

# Making methods for functionallity
clients=[]
nicknames=[]

#broadcast method
def broadcast(message):
    for client in clients:
        client.send(message)

#handle the client properly
def handle(client):
    while True:
        try:
            
            message = client.recv(1024)
            broadcast(message)
            
	    
	    
            
	    
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            broadcast(f'{nickname }left the chat'.encode('ascii'))
            
            nicknames.remove(nickname)
            break

# the recieve method
def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with{str(address)}")

        client.send("GTG".encode('ascii'))

        nickname = client.recv(1024).decode('ascii')

        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname of the client is {nickname}!')

        broadcast(f'{nickname} joined the chat'.encode('ascii'))

        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle,args=(client,))
        
        thread.start()

print("Server is listening...")

recieve()

        
              
        
        
            





