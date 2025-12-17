from problema2.repository.client_repository import ClientRepository, DuplicateIdError


class ClientFileRepository(ClientRepository):

    def __init__(self, filename):
        super().__init__()
        self.filename=filename
        self.__load_data()

    def __load_data(self):
        with open(self.filename) as f:
            for line in f:
                lista_client=line.split(",")
                from problema2.domain.client import Client
                client=Client(int(lista_client[0]), lista_client[1], int(lista_client[2]))
                super().save(client)

    def save(self, client):
            super().save(client)
            self.__add_to_file(client)

    def __add_to_file(self, client):
        with open(self.filename, "a") as f:
            string_client="\n"+str(client.get_id())+","+client.get_nume()+","+str(client.get_CNP())
            f.write(string_client)

    def __update_to_file(self, client):
        with open(self.filename, "a") as f:
            for line in f:
                pass

#todo: stergere,modificare