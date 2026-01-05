from domain.entities import Client
from domain.validators import IdNotFoundError
from repository.client_repository import ClientRepository


class ClientFileRepository(ClientRepository):
    def __init__(self, validator, filename ):
        super().__init__(validator)
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
        try:
            self.__update_to_file()
        except IdNotFoundError :
            print("Acest id nu este scris in lista")


    def delete_by_id(self, client):
        try:
            super().delete_by_id(client.id)
        except IdNotFoundError as m:
            print(m)
        self.__rewrite()

    def __add_to_file(self, client):
        with open(self.__filename, "a") as f:
            string_client = str(client.id) + "," + client.nume + "," + str(client.CNP)
            f.write(string_client)


    def __rewrite(self):
        lista_clienti=self.find_all()
        with open(self.__filename, "w") as f:
            for client in lista_clienti:
                client_file=str(client.id)+","+str(client.nume)+","+str(client.CNP)+"\n"
                f.write(client_file)


    def __update_to_file(self):
        lista_clienti = self.find_all()
        with open(self.__filename, "w") as f:
            for client in lista_clienti:
                client_file = str(client.id) + "," + str(client.nume) + "," + str(client.CNP) + "\n"
                f.write(client_file)

    def find_by_id_f(self, id):
       return  super().find_by_id(id)



