from client_operations.clients import clients
from client_operations.client_repited import isRepeteadClient
from client_operations.get_client_field import __get_client_field

def update_client(client_to_change):
	for i, client in enumerate(clients):
		if client_to_change == clients[i].get('name'):
			print("\n\n\tOk, now the fields to update\n")
			client = {
                'name': __get_client_field('name'),
                'company': __get_client_field('company'),
                'email': __get_client_field('email'),
                'position': __get_client_field('position')
            }
			clients[i] = client
			print('''\nvery well, you updated the fields of client {} called {}'''.format(i, client_to_change))
			return True
	print('''\nLo siento, no hay ninguna persona que se llame ''' + client_to_change)
