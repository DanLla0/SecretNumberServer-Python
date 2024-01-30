import socket
import ipaddress
import random

HOST = "localhost"
PORT = 2000
n = random.randint(1,10)
print(f"Número secreto: {n}")
#para comprobar si el puerto está escuchando netstat -a en cmd (conexiones activas ahora en el ordenador)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))#los dos parentesis son obligatorios
s.listen()
print("Servidor abierto") 
conn,addr = s.accept()#espera al cliente
print(f"conexion con el cliente IP: {addr[0]} Puerto: {addr[1]} ha sido completada")
code = "0"
mess = ""
while True:
    data=conn.recv(1024)
    if data.decode() != '':
        if int(data.decode())==n:
            code = "-1"
            mess = "Has acertado, el número secreto era: "+str(n)
        else:           
            if int(data.decode())<n:
                mess = "El número es mayor"
            else:
                mess = "El número es menor"
            code = str(n)
        conn.send(code.encode())
        conn.send(mess.encode())
    else:
        print(f"conexion con el cliente IP: {addr[0]} Puerto: {addr[1]} ha sido cerrada")
        break
conn.close()
