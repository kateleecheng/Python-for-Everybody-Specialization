# ord() for ASSII code
import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80)) #(host,port)
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()#Bytes
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
        mystring=data.decode()
        #mystring=unicode
        #data=bytes(UTF-8 or ASCII)
    print(data.decode())
mysock.close()
