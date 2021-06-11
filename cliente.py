import socket

mi_socket = socket.socket()
# Direccdion a conectar y puerto
mi_socket.connect(('localhost', 4040))

mi_socket.send("Hola desde el cliente")
respuesta = mi_socket