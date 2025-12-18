from domain.entities import Client
from domain.validators import IdNotFoundError, DuplicateIdError
from repository.client_repository import ClientRepository


class IsNotCnpError(Exception):
    pass

class ClientService:
    def __init__(self, client_repository):
        self.__client_repository = client_repository

    def add_client(self, id, nume, CNP):
        if len(str(CNP)) != 13:
            raise IsNotCnpError("Nu are forma de cnp")
        client=Client(id, nume, CNP)
        try:
            self.__client_repository.save(client)
        except DuplicateIdError:
            print("Duplicate id")

    def remove_client(self, id):
        id=int(id)
        c=self.find_by_id_s(id)
        self.__client_repository.delete_by_id_f(c)

    def get_all_client(self):
        return self.__client_repository.find_all()

    def modify_client(self, id, nume, CNP):
        client=Client(id, nume, CNP)
        try:
            self.__client_repository.update(client)
        except IdNotFoundError:
            print("Nu exista acest id")

    def find_by_id_s(self, id):
        return self.__client_repository.find_by_id_f(id)



if __name__=="__main__":
    client_repository=ClientRepository()
    service=ClientService(client_repository)
    service.add_client(1, "ana", 1234)
    service.add_client(2, "ana", 1234)
    service.add_client(3, "ana", 1234)
    service.get_all_client()