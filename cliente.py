import socket

mi_socket = socket.socket()
# Direccdion a conectar y puerto
mi_socket.connect(('localhost', 4040))

txt = "Hola desde el cliente"
mi_socket.send(txt.encode("ascii"))
# 1024 hace referencia al buffer en bits
respuesta = mi_socket.recv(1024)
txt_respuesta = respuesta.decode("ascii")

print (txt_respuesta)
mi_socket.close()