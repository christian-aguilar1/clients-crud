import csv
import os

CLIENT_TABLE = ".clients.csv"
CLIENT_SCHEMA = ["name", "company", "email", "position"]
clients = []


def initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode="r") as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def save_clients_to_storage():
    tmp_table_name = "{}.tmp".format(CLIENT_TABLE)
    with open(tmp_table_name, mode="w") as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)
