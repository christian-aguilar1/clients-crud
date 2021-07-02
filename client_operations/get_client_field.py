def __get_client_field(field_name):
    while True:
        field = input('''What is the client {}?: '''.format(field_name)).lower().capitalize()
        if field != "":
            break
        else:
            print("\nSorry, you can\'t leave the field empty, write it again\n")

    return field