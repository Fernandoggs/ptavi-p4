#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

#Manejador de datagramas
#Un servidor echo es un servidor que envia lo mismo que recibe
class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        print('Ip_Cliente: ' + self.client_address[0])
        print('Puerto_Cliente: ' + str(self.client_address[1]))
        self.wfile.write(b"Hemos recibido tu peticion")
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))

if __name__ == "__main__":
	#Crea un servidor UDP.Hay q pasar 2 parametros: ip y puerto donde voy a escuchar /
	# y la clase 
    serv = socketserver.UDPServer(('', int(sys.argv[1])), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    #Se crea esta excepción para q al salir del servidor con crtl+c salga el mensaje de Finalizado
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")