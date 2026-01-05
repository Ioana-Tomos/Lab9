import unittest

from domain.entities import Film


class ClientTestCase(unittest.TestCase):


    def test_get_id(self):
        self.film = Film(1, "Titanic", "dsufbfer regregre", "drama")
        assert (self.film.id == 1)
        self.film.id=2
        assert (self.film.id == 2)


    def test_get_set_titlu(self):
        self.film = Film(1, "Titanic", "dsufbfer regregre", "drama")
        assert (self.film.titlu== "Titanic")
        self.film.titlu="Razboiul stelelor"
        assert (self.film.titlu == "Razboiul stelelor")


    def test_get_set_descriere(self):
        self.film = Film(1, "Titanic", "dsufbfer regregre", "drama")
        assert (self.film.descriere == "dsufbfer regregre")
        self.film.set_descriere="ABCDEFG"
        assert (self.film.descriere() == "ABCDEFG")


    def test_get_set_gen(self):
        self.film = Film(1, "Titanic", "dsufbfer regregre", "drama")
        assert (self.film.gen == "drama")
        self.film.gen="wefdfdfd"
        assert (self.film.gen == "wefdfdfd")


    # def all_teste_filme():
    #     test_get_id()
    #     test_get_set_titlu()
    #     test_get_set_descriere()
    #     test_get_set_gen()
