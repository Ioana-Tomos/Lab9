import unittest

from domain.entities import Client
from repository.client_repository import ClientRepository


class ClientTestCase(unittest.TestCase):

    # def setUp(self):
    #     client1=Client(1, "Ana", 1234567890123)
    #     client2=Client(2, "Maria", 1345678901234)
    #     self.clientrepositori=ClientRepository
    #     self.clientrepositori.save(client1)
    #     self.clientrepositori.save(client2)

    def test_get_set_id(self):
        self.client = Client(1, "ana", 409874321)
        assert (self.client.id == 1)
        self.client.id(2)
        assert (self.client.id == 2)


    def test_get_set_name(self):
        self.client = Client(1, "ana", 409874321)
        assert (self.client.nume == "ana")
        self.client.nume="Ana"
        assert (self.client.nume == "Ana")


    def test_get_set_CNP(self):
        self.client = Client(1, "ana", 409874321)
        assert (self.client.CNP == 409874321)
        self.client.CNP(235)
        assert (self.client.CNP == 235)

    # def all_teste_clienti(self):
    #     test_get_set_id()
    #     test_get_set_name()
    #     test_get_set_CNP()
