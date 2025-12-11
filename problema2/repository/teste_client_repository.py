import unittest

from problema2.domain.client import Client
from problema2.repository.client_repository import ClientRepository, DuplicateIdError

class ClientRepositoryTestCase(unittest.TestCase):


    def test_save(self):
        client = Client(1, "Ana", 2345678901234)
        self.client_repo = ClientRepository()
        assert (len(self.client_repo.find_all()) == 0)
        self.client_repo.save(client)
        assert (len(self.client_repo.find_all()) == 1)
        assert (self.client_repo.find_all()[0].get_id() == client.get_id())
        assert (self.client_repo.find_all()[0].get_nume() == client.get_nume())
        assert (self.client_repo.find_all()[0].get_CNP() == client.get_CNP())
        try:
            self.client_repo.save(client)
            assert False
        except DuplicateIdError:
            assert True


    def test_find_all(self):
        self.client_repo=ClientRepository()
        client=Client(1, "Ana", 12345678901234)
        assert (isinstance(self.client_repo.find_all(), list) )
        assert (len(self.client_repo.find_all()) == 0)
        self.client_repo.save(client)
        assert (self.client_repo.find_all()[0].get_id()==client.get_id())
        assert (self.client_repo.find_all()[0].get_nume() == client.get_nume())
        assert (self.client_repo.find_all()[0].get_CNP() == client.get_CNP())

    def test_update(self):
        self.client_repo=ClientRepository()
        client = Client(1, "Ana", 2345678901234)
        client2=Client(1, "Dana", 2345678901274)
        self.client_repo.save(client)
        assert(self.client_repo.find_all()[0].get_id()==client.get_id())
        assert (self.client_repo.find_all()[0].get_nume() == client.get_nume())
        assert (self.client_repo.find_all()[0].get_CNP() == client.get_CNP())
        self.client_repo.update(client2)
        assert (self.client_repo.find_all()[0].get_id() == client2.get_id())
        assert (self.client_repo.find_all()[0].get_nume() == client2.get_nume())
        assert (self.client_repo.find_all()[0].get_CNP() == client2.get_CNP())

    def test_delete_by_id(self):
        self.client_repo=ClientRepository()
        client=Client(1, "Ana", 2345678901234)
        client2=Client(2, "Dana", 234567890124)
        self.client_repo.save(client)
        self.client_repo.save(client2)
        self.client_repo.delete_by_id(client.get_id())
        assert (self.client_repo.find_all()[0].get_id() == client2.get_id())
        assert (self.client_repo.find_all()[0].get_nume() == client2.get_nume())
        assert (self.client_repo.find_all()[0].get_CNP() == client2.get_CNP())

    # def test_all_client_repository():
    #     test_save()
    #     test_find_all()
    #
    #     test_update()
    #     test_delete_by_id()