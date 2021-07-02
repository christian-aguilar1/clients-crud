from client_operations.clients import clients


def search_client(client_name):
    for client in clients:
        if client_name == client.get("name", ""):
            return True
