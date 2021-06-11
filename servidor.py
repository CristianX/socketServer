import socket

mi_socket = socket.socket()
mi_socket.bind(('localhost', 4040))
# las conexiones en cola que pueden estar (5)
mi_socket.listen(5)

while True:
    # Aceptando peticiones (Retornando dos valores "conexion" y direccion)
    conexion, addr = mi_socket.accept()
    print ("Nueva conexiónn establecida!")
    print (addr)

    conexion.send("Hola, te saludo desde el servidor!")
    conexion.close()