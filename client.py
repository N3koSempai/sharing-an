# client.py
import os
import socket
import struct



def send_file(sck: socket.socket, filename):
    # Obtener el tamaño del archivo a enviar.
    filesize = os.path.getsize(filename)
    # Informar primero al servidor la cantidad
    # de bytes que serán enviados.
    sck.sendall(struct.pack("<Q", filesize))
    # Enviar el archivo en bloques de 1024 bytes.
    with open(filename, "rb") as f:
        while read_bytes := f.read(1024):
            sck.sendall(read_bytes)
    
def start(file):    
    with socket.create_connection(("localhost", 6190)) as conn:
        print("Conectado al servidor.")
        print("Enviando archivo...")
        send_file(conn, file)
        print("Enviado.")

while True:
    file = input("Enter the url and the name of your file with extension example: ./example.exa \n ==> ")
    
    x= input("write yes for send or anything for cancel \n ==> ")
    if x == "yes" or x == "y":
        start(file)
    else:
        break
print("Conexión cerrada.")








