import socket
import ipaddress

HOST = "localhost"
PORT = 2000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # sock stream es que vamos a intercambiar datos
s.connect((HOST,PORT))
print(f"Conectado con exito")
attempts = 10
while attempts > 0:
    n = input("Dime un número:")
    s.send(n.encode())
    print(s.recv(1024).decode())
    if s.recv(1024).decode() == "1":
        break
    attempts = attempts-1
s.close()
