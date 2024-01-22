import socket
import ipaddress
import random

HOST = "localhost"
PORT = 2000
n = random.randint(1,10)
print(f"Número secreto : {n}")
#para comprobar si el puerto está escuchando netstat -a en cmd (conexiones activas ahora en el ordenador)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))#los dos parentesis son obligatorios
s.listen()#abrimos servidor
print("Servidor abierto") 
conn,addr = s.accept()#espera al cliente
code = "0"
while True:
    data=conn.recv(1024)  
    if int(data.decode())==n:
        code = "1"
        break
    else:
        if int(data.decode())<n:
            conn.send("El número es mayor".encode())
        else:
            conn.send("El número es menor".encode())
        conn.send(code.encode())
mess = "Has acertado, el número secreto era: "+str(n)
conn.send(mess.encode())
conn.send(code.encode())
conn.close()
