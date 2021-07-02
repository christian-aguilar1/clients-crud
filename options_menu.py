import re

from client_operations.clients import initialize_clients_from_storage
from client_operations.clients import save_clients_to_storage
from client_operations.get_client_field import __get_client_field

from CRUD.create_client import create_client
from CRUD.delete_client import delete_client
from CRUD.read_clients import read_clients
from CRUD.search_client import search_client
from CRUD.update_client import update_client

from default_phrases import option_invalid
from sys_operations.clear_screen import clear_screen
from sys_operations.key_pressed import key_pressed


def menu_opciones():
    initialize_clients_from_storage()
    while True:
        # clear_screen()
        opcion_elegida = input(
            """\n\n\tWelcome!

Which option do you want to choose?:

\t1. Create a new client
\t2. Read clients
\t3. Update a client
\t4. Delete a client
\t5. Search a client
\t6. Exit

Opción: """
            ""
        )

        if opcion_elegida == "1":
            clear_screen()
            print("""\n\n\tWell! You chose option 1, create a new client \n""")
            client = {
                "name": __get_client_field("name"),
                "company": __get_client_field("company"),
                "email": __get_client_field("email"),
                "position": __get_client_field("position"),
            }
            create_client(client)
            key_pressed()
            clear_screen()
        elif opcion_elegida == "2":
            clear_screen()
            print("""\n\tWell! You chose option 2, read clients""")
            read_clients()
            key_pressed()
            clear_screen()
        elif opcion_elegida == "3":
            clear_screen()
            print("""\n\tWell! You chose option 3, update a client old\n""")
            # update = update_client(__get_client_field("name to update"))
            update_client(__get_client_field("name to update"))
            key_pressed()
            clear_screen()
        elif opcion_elegida == "4":
            clear_screen()
            print("""\nWell! You chose option 4, delete a client\n""")
            delete_client(__get_client_field("name"))
            key_pressed()
            clear_screen()
        elif opcion_elegida == "5":
            clear_screen()
            print("""\nWell! You chose option 5, search a client\n""")
            client_to_search = __get_client_field("name")
            found = search_client(client_to_search)
            if found:
                print("""\nThe client is found in the client list""")
            else:
                print(
                    """\nThe client""",
                    client_to_search,
                    """isn't found in the client list""",
                )
            key_pressed()
            clear_screen()
        elif opcion_elegida == "6":
            clear_screen()
            print("""\nOk see you. Until next time! :D""")
            key_pressed()
            break
        else:
            clear_screen()
            print(option_invalid)
            key_pressed()
            clear_screen()

    save_clients_to_storage()


def __get_client_name():
    client_name = None

    while True:
        client_name = input("""\nCual es el nombre del cliente?: """)
        if re.search("[0-9]", client_name):
            print(option_invalid)
        elif client_name.isalpha():
            break

    return client_name
