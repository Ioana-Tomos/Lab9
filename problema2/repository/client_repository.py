from domain.validators import DuplicateIdError, IdNotFoundError


class ClientRepository:
    def __init__(self, validator):
        self.__all_clients = {}
        self.__validator = validator

    def find_all(self):
        return list(self.__all_clients.values())

    def save(self, client):
        self.__validator.validate(client)
        if self.find_by_id(client.id) is not None:
            raise DuplicateIdError("duplicat")
        self.__all_clients[client.id] = client

    def update(self, client):
        self.__validator.validate(client)
        if self.find_by_id(client.id) is None:
            raise IdNotFoundError("Acest id nu exista in lista")
        else:
            self.__all_clients[client.id] = client

    def delete_by_id(self, idu):
        if self.find_by_id(idu) is None:
            raise IdNotFoundError("Id-ul nu este")
        else:
            self.__all_clients.pop(idu)

    def find_by_id(self, id_client):
        for i in self.__all_clients.values():
            if i.id == id_client:
                return i
        return None

    def __add_to_file(self, student):
        pass
