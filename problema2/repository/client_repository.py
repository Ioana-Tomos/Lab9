class IdNotFoundCError(Exception):
    pass
class DuplicateIdError(Exception):
    pass

class ClientRepository:
    def __init__(self):
        self.__all_clients = {}

    def find_all(self):
        return list(self.__all_clients.values())

    def save(self, client):
        if self.find_by_id(client.get_id()) is not None:
            raise DuplicateIdError("duplicat")
        self.__all_clients[client.get_id()] = client

    def update(self, client):
        if self.find_by_id(client.get_id()) is None:
            raise IdNotFoundCError("Acest id nu exista in lista")
        else:
             self.__all_clients[client.get_id()] = client

    def delete_by_id(self, id):
        if self.find_by_id(id) is None:
            raise IdNotFoundCError("Id-ul nu este")
        self.__all_clients.pop(id)

    def find_by_id(self, id_client):
        for i in self.__all_clients.values():
            if i.get_id() ==id_client:
                return id_client
        return None

    def __add_to_file(self, student):
        pass