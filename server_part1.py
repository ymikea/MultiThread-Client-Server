from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM) 
serverName= 'localhost'
serverPort= 8000
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print ("The server is ready to receive on port 8000")

while True:
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    try: 
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        
        f = open(filename[1:],errors='ignore')
        outputdata = f.read()
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 
    except IOError:
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close() 
serverSocket.close()
sys.exit()