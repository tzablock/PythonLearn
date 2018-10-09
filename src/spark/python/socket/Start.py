import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)

server = 'pythonprogramming.net'
port = 80
request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

server_ip = socket.gethostbyname(server)
print(server_ip)

s.connect((server,port))
s.send(request.encode())

response = s.recv(4096)
while(len(response)>0):
    print(response)
    response = s.recv(4096)
