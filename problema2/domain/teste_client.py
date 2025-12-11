import unittest

from problema2.domain.client import Client

class ClientTestCase(unittest.TestCase):
    def test_get_set_id(self):
        self.client = Client(1, "ana", 409874321)
        assert (self.client.get_id() == 1)
        self.client.set_id(2)
        assert (self.client.get_id() == 2)


    def test_get_set_name(self):
        self.client = Client(1, "ana", 409874321)
        assert (self.client.get_nume() == "ana")
        self.client.set_nume("Ana")
        assert (self.client.get_nume() == "Ana")


    def test_get_set_CNP(self):
        self.client = Client(1, "ana", 409874321)
        assert (self.client.get_CNP() == 409874321)
        self.client.set_CNP(235)
        assert (self.client.get_CNP() == 235)


    # def all_teste_clienti(self):
    #     test_get_set_id()
    #     test_get_set_name()
    #     test_get_set_CNP()
