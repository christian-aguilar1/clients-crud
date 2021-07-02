from client_operations.clients import clients


def delete_client(client_name):
    for i in clients:
        print(i)
        if client_name == i.get("name"):
            while True:
                opcion_elegida = input(
                    """\nAre you sure you want to delete this client?\n\nSelecciona\n\n(s) si\n\n(n) no\n\n"""
                )
                if opcion_elegida.lower() == "s":
                    clients.remove(i)
                    print("\nSuccessfully removed client")
                    return True
                elif opcion_elegida.lower() == "n":
                    print("\nRequest accepted. The process was canceled")
                    return True
                else:
                    print("""\nThis option is invalid, please try again""")
        return True
    print("""This client isn\'t added""")
    return True
