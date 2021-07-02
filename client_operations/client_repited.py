from client_operations.clients import clients

def isRepeteadClient(client_name):
	for current_client in clients:
		if client_name == current_client:
			return True
		else:
			return False