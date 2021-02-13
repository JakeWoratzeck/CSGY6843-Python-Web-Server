#Jake Woratzeck JCW9324
#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)

   #Prepare a sever socket
   #Fill in start
   serverSocket.bind(('127.0.0.1', port))
   serverSocket.listen(1)
   connection = True
   #Fill in end

   while connection == True:
       #Establish the connection
       #Is this breaking Gradescope? I saw this on the Slack...
       #print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept()#Fill in start      #Fill in end
       try:
            message = connectionSocket.recv(1024)#Fill in start    #Fill in end
           
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()#Fill in start     #Fill in end

            #Send one HTTP header line into socket
            #Fill in start
            #Send a 200 OK if the connection worked
            #Check if connection is closed before sending anything
            
            connectionSocket.send(('HTTP/1.1 200 OK\r\n\r\n').encode())
            
            #Fill in end

            #Send the content of the requested file to the client
            
            for i in range(0, len(outputdata)):
                if not message:
                    break
                else:
                    connectionSocket.send(outputdata[i].encode())
            
            connectionSocket.send("\r\n\r\n".encode())
            connectionSocket.close()
            connection=False
       except IOError:
           #Send response message for file not found (404)
           #Fill in start
           #send a 404 if the connection did NOT work
           #If the connection is already closed, don't try to send anything else
            if not message:
                break
            else:
                connectionSocket.send(('HTTP/1.1 404 Not Found\r\n\r\n').encode())
            #connectionSocket.send(bytes("404 Not Found", "UTF-8"))
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            connection = False
            
            #  Fill in end

   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)
