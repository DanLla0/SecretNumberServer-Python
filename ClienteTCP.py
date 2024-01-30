import socket
import ipaddress
import math

HOST = "localhost"
PORT = 2000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # sock stream es que vamos a intercambiar datos
s.connect((HOST,PORT))
print(f"Conectado con exito")
attempts = 4
code = 0
while attempts > 0:
        n = input("Dime un número:")
        s.send(n.encode())
        code = s.recv(1024).decode() 
        if code == "-1":
            print(s.recv(1024).decode())
            break
        else:
            print(s.recv(1024).decode())
        attempts = attempts-1    
if attempts == 0:
    print(f"Te has quedado sin intentos.")
    print(f"El número secreto era: {code}")
s.close()
