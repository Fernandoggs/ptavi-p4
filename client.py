#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
server_ip = sys.argv[1]
port = int(sys.argv[2])
if not sys.argv[3] == 'register':
    sys.exit("Usage: client.py ip puerto register sip_address")
sip_address = sys.argv[4]
#line = ' '.join(sys.argv[3:])
line = 'REGISTER sip:' + sip_address + ' SIP/2.0\r\n'


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((server_ip, port))
    print("Enviando:", line)
    my_socket.send(bytes(line, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
