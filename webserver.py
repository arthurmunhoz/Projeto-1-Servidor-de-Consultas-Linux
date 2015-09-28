#!/usr/bin/python

print('Content-type: text/html\n')

print """
	<html>
	<title>TRABALHO 1 - REDES DE COMPUTADORES</title>
	<body>
		<form method=POST action="cgi-bin/backend.py">
			<P><strong>TRABALHO 1 - REDES DE COMPUTADORES</strong><br><br><strong>Bem vindo!</strong><br>Escolha as operacoes que desejar: <br><br>
		
			<strong>Maquina 1:</strong><br>
			<input type="checkbox" name="m1ps" value="1"> Executar: ps<br>
			<input type="checkbox" name="m1df" value="2"> Executar: df<br>
			<input type="checkbox" name="m1finger" value="3"> Executar: finger<br>
			<input type="checkbox" name="m1uptime" value="4"> Executar: uptime<br>

			<br>
			<input type=submit name="btnEnviar">
		</form>
	</body></html>

"""
