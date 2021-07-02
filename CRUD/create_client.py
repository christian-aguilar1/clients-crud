from client_operations.clients import clients
from client_operations.client_repited import isRepeteadClient

def create_client(client):
	if isRepeteadClient(client['name'].lower().capitalize()):
		print('''\nLo siento, no se pudo agregar el nombre, este cliente ya estaba agregado''')
	else:
		clients.append(client)
		print('''\nMuy bien!, nombre agregado con exito\n''')
