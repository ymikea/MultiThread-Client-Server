
from socket import *
import sys
from threading import Thread, activeCount


def request(connectionSocket,clientInfo):
    print("client {} has connected".format(clientInfo))
    try: 
        message = connectionSocket.recv(1024).decode()              #recieve message from the client
        filename = message.split()[1]                               #client send the html file name
        f = open(filename[1:])                                      
        outputdata = f.read()
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())     #send 200 OK first status to client to send the entire html data
        for i in range(0, len(outputdata)):                         #send the entire html data
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close()                                    #close the connection
    except IOError:
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())  #if file that client send doesn't exit in server
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()) #send Not founf status
        connectionSocket.close()                                    #close the connection


def main():
    #Prepare the server
    serverName= 'localhost'
    serverPort= 8000
    serverSocket = socket(AF_INET, SOCK_STREAM)                     
    serverSocket.bind((serverName,serverPort))
    serverSocket.listen(5)
    print ("The server is ready to receive on port 8000")

    while True:
        #Establish connection and start thread, respond to the requests 
        print('Ready to serve...') 
        connectionSocket, addr = serverSocket.accept()
        process = Thread(target=request, args=(connectionSocket, addr))
        process.start()
        print(f"[Active threads] {activeCount() - 1}") #will print the threads that are connected to server
    serverSocket.close()

if __name__ == '__main__':
	main()