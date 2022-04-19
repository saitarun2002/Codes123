#UDPServer.py
from socket import *
serverPort = 1200
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("localhost", serverPort))

print ("The server is ready to receive")
while 1:
    b, clientAddress = serverSocket.recvfrom(1200)
    message=b.decode()
    print(message)
    modifiedMessage = message.upper()
    c=modifiedMessage.encode()
    serverSocket.sendto(c, clientAddress)

#UDPClient.py
from socket import *
serverName = "localhost"
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input lowercase sentence:")
b=message.encode()
clientSocket.sendto(b,(serverName, serverPort))
c, serverAddress = clientSocket.recvfrom(1200)
modifiedMessage=c.decode()
print (modifiedMessage)
clientSocket.close()

#TCPServer.py
from socket import *
serverPort = 1200
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    b = connectionSocket.recv(1200)
    message=b.decode()
    modifiedMessage = message.upper()
    c=modifiedMessage.encode()
    connectionSocket.send(c)
    connectionSocket.close()

#TCPClient.py
from socket import *

serverName = "localhost"
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input("Input lowercase sentence:")
b=message.encode()
clientSocket.sendto(b,(serverName, serverPort))

c, serverAddress = clientSocket.recvfrom(1200)
modifiedMessage=c.decode()
print (modifiedMessage)
clientSocket.close()


#Server.py
from socket import *
serverPort = 1201
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("localhost", serverPort))
print ("The server is ready to receive")
while 1:
    b, clientAddress = serverSocket.recvfrom(1201)
    message=b.decode()
    print(message)
    replymessage = input("Server:")
    print(replymessage)
    c=replymessage.encode()
    serverSocket.sendto(c,clientAddress)

#Client.py
from socket import *
serverName = "localhost"
serverPort = 1201
#for i in range (0,10):
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Client:")
b=message.encode()
clientSocket.sendto(b,(serverName, serverPort))
c, serverAddress = clientSocket.recvfrom(1201)
modifiedMessage=c.decode()
print (modifiedMessage)
clientSocket.close()

#!
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class Client1 {
    public static void main(String[] args) {

        System.out.println("I am client");
try {
    Socket client =new Socket("localhost", 5003);

    DataInputStream cdi = new DataInputStream(client.getInputStream());
    DataOutputStream cdo = new DataOutputStream(client.getOutputStream());

    String input = (String)cdi.readUTF();

System.out.println("Server Message" +input);

//Scanner sc =new Scanner(System.in);

//String output = sc.nextLine();

//cdo.writeUTF(output);
//cdo.flush();

} catch (Exception e) {
    //TODO: handle exception
}
        
    }
}


#
import java.net.*;
import java.io.*;
import java.util.*;
public class Server1 {
public static void main(String[] args) {
    try {
        System.out.println("I am a server");
        ServerSocket ss = new ServerSocket(5003);

        Socket client=ss.accept();

        DataInputStream cdi = new DataInputStream(client.getInputStream());
    DataOutputStream cdo = new DataOutputStream(client.getOutputStream());

//    String input = (String)cdi.readUTF();

//System.out.println("Server Message" +input);

Scanner sc =new Scanner(System.in);

String output = sc.nextLine();

cdo.writeUTF(output);
cdo.flush();
    } catch (Exception e) {
        //TODO: handle exception
    }
}
}





