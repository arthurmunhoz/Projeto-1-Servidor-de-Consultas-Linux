#!/usr/bin/python

import cgi
import os

form = cgi.FieldStorage()                 # coleta dados do form de webserver.py

print('Content-type: text/html\n')        # define o tipo de conteudo para o restante do programa
print('<title>TRABALHO 1 - REDES DE COMPUTADORES</title>')        # titulo da pagina html

#exemplo para updates futuros no codigo de como capturar valores
# Verificando se o usuario digitou o nome
#if not 'user' in form:
#    print('<h1>Who are you?</h1>')
#else:
#    print('<h1>Ola <i>%s</i>!</h1>' % cgi.escape(form['user'].value))

# Verificando quais opcoes foram selecionadas para MAQUINA 1
if 'm1ps' in form:
	print('MAQUINA 1: PS <br><br>')
if 'm1df' in form:
	print('MAQUINA 1: DF <br><br>')
if 'm1finger' in form:
	print('MAQUINA 1: FINGER <br><br>')
if 'm1uptime' in form:
	print('MAQUINA 1: UPTIME <br><br>')

