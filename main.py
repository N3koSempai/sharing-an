# server.py
import socket
import struct
import os
def receive_file_size(sck: socket.socket):
    # Esta función se asegura de que se reciban los bytes
    # que indican el tamaño del archivo que será enviado,
    # que es codificado por el cliente vía struct.pack(),
    # función la cual genera una secuencia de bytes que
    # representan el tamaño del archivo.
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()
    while received_bytes < expected_bytes:
        chunk = sck.recv(expected_bytes - received_bytes)
        stream += chunk
        received_bytes += len(chunk)
    filesize = struct.unpack(fmt, stream)[0]
    return filesize
def receive_file(sck: socket.socket, filename):
    # Leer primero del socket la cantidad de 
    # bytes que se recibirán del archivo.
    filesize = receive_file_size(sck)
    # Abrir un nuevo archivo en donde guardar
    # los datos recibidos.
    with open(filename, "wb") as f:
        received_bytes = 0
        # Recibir los datos del archivo en bloques de
        # 1024 bytes hasta llegar a la cantidad de
        # bytes total informada por el cliente.
        while received_bytes < filesize:
            chunk = sck.recv(1024)
            if chunk:
                f.write(chunk)
                received_bytes += len(chunk)
                
                
def start(default):
    if default == None:
        default = os.path.realpath(__file__)
    try:    
        os.chdir(default)
    except FileNotFoundError:
        default = os.path.realpath(__file__)
        os.chdir(default)
    with socket.create_server(("localhost", 6190)) as server:
        print("Esperando al cliente...")
        conn, address = server.accept()
        print(f"{address[0]}:{address[1]} conectado.")
        print("Recibiendo archivo...")
        receive_file(conn, "imagen-recibida.png")
        print("Archivo recibido.")

default = input("Select you default folder example: ./example/example.txt \n ==>")
start(default)
print("Conexión cerrada.")








