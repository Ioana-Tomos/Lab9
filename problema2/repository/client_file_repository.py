from domain.entities import Client
from domain.validators import IdNotFoundError
from repository.client_repository import ClientRepository


class ClientFileRepository(ClientRepository):

    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_data()

    def __load_data(self):
        with open(self.__filename) as f:
            for line in f:
                lista_client = line.split(",")
                client = Client(int(lista_client[0]), lista_client[1], int(lista_client[2]))
                super().save(client)

    def save(self, client):
        super().save(client)
        self.__add_to_file(client)

    def update(self, client):
        super().update(client)
        self.__update_to_file(client)

    def delete_by_id(self, id):
        try:
            super().delete_by_id(id)
        except IdNotFoundError as m:
            print(m)

        c = super().find_by_id(id)
        print(c)
        self.__remove_from_file(c)

    def __add_to_file(self, client):
        with open(self.__filename, "a") as f:
            string_client = "\n" + str(client.id) + "," + client.nume + "," + str(client.CNP)
            f.write(string_client)

    def __remove_from_file(self, client):
        with open(self.__filename, "r+") as f:
            string_client = "\n" + str(client.id) + "," + str(client.nume) + "," + str(client.CNP)
            text = f.readlines()
            f.seek(0)
            for line in text:
                if line != string_client:
                    f.write(line)

            # for line in f:
            #     copy_line=line.split(",")
            #     string_client="\n"+str(client.id)+","+str(client.nume)+","+str(client.CNP)
            #     if copy_line[0]==string_client[0]:
            #         line.replace(string_client)

    def __update_to_file(self, client):
        with open(self.__filename, "a") as f:
            for line in f:
                lista_client = line.split(",")
                if client.id == lista_client[0]:
                    pass

    def find_by_id(self, id):
        super().find_by_id(id)

# todo: stergere,modificare
