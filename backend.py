#!/usr/bin/python

import cgi
import cgitb
import os
from socket import *

form = cgi.FieldStorage()                 # coleta dados do form de webserver.py

serverName = 'localhost'
serverPort = 12000
backendSocket = socket(socket.AF_INET,socket.SOCK_DGRAM)

backendSocket.bind(('', serverPort))

backendSocket.listen(3)

print('Content-type: text/html\n')        # define o tipo de conteudo para o restante do programa
print('<title>TRABALHO 1 - REDES DE COMPUTADORES</title>')        # titulo da pagina html
# para cada comando selecionado faz um request
if 'm1ps' in form:
	backendSocket.sendto("REQUEST " + cgi.escape(form['m1ps'].value, (serverName, serverPort))
	response = clientSocket.recvfrom(2048)
	print('<h1>PS: %s</h1><br><br>' %response)
if 'm1df' in form:
	backendSocket.sendto("REQUEST " + cgi.escape(form['m1df'].value, (serverName, serverPort))
	response = clientSocket.recvfrom(2048)
	print('<h2>RESPONSE: %s</h2><br><br>' %response)
if 'm1finger' in form:
	backendSocket.sendto("REQUEST " + cgi.escape(form['m1finger'].value, (serverName, serverPort))
	response = clientSocket.recvfrom(2048)
	print('<h3>RESPONSE FINGER: %s</h3><br><br>' %response)
if 'm1uptime' in form:
	backendSocket.sendto("REQUEST " + cgi.escape(form['m1uptime'].value, (serverName, serverPort))
	response = clientSocket.recvfrom(2048)
	print('<h4>RESPONSE UPTIME: %s</h4><br><br>' %response)
	
backendSocket.close()




