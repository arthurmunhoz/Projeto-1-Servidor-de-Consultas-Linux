#!/usr/bin/python

from socket import *
from os import *

serverName = 'localhost'
serverPort = 12000

daemonSocket = socket(socket.AF_INET,socket.SOCK_DGRAM)

request, backendAddress = clientSocket.recvfrom(2048)

if request == "REQUEST 1"
	response = "RESPONSE ps: " + system("ps")
	daemonSocket.sendto(response, backendAddress)
if request == "REQUEST 2"
	response = "RESPONSE df: " + system("df")
	daemonSocket.sendto(response, backendAddress)
if request == "REQUEST 3"
	response = "RESPONSE finger: " + system("finger")
	daemonSocket.sendto(response, backendAddress)
if request == "REQUEST 4"
	response = "RESPONSE uptime: " + system("uptime")
	daemonSocket.sendto(response, backendAddress)

daemonSocket.close()
