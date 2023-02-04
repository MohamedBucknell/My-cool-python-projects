import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1',55555))

nickname = input("Chose a nickname: ")+""

def recieve():
    while True:
        try:
            
            message = client.recv(1024).decode('ascii')
            if message == "GTG":
                client.send(nickname.encode('ascii'))

                pass
                                    

                
            
                    
            else:
                    print(message)
        except:
            print("An error occured! ")
            client.close()
            break

def write():

    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))




recieve_thread = threading.Thread(target= recieve)
recieve_thread.start()

write_thread = threading.Thread(target= write)
write_thread.start()



        
