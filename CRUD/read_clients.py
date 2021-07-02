from client_operations.clients import clients

def read_clients():
	print_clients = ''
	large_list_clients = len(clients) - 1
	if len(clients) == 0:
		print('''\n\tNo clients added yet''')
		return True
	else:
		print('''\n\tClients are: \n''')
		for idx, client in enumerate(clients):
			print('{uid} | {name} | {company} | {email} | {position}'.format(
				uid = idx,
				name = clients[idx].get('name', ''),
				company = clients[idx].get('company', ''),
				email = clients[idx].get('email', ''),
				position = clients[idx].get('position', '')
			))
