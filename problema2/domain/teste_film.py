import unittest

from domain.entities import Film


class ClientTestCase(unittest.TestCase):


    def test_get_id(self):
        self.film = Film(1, "Titanic", "dsufbfer regregre", "drama")
        assert (self.film.get_id() == 1)
        self.film.set_id(2)
        assert (self.film.get_id() == 2)


    def test_get_set_titlu(self):
        self.film = Film(1, "Titanic", "dsufbfer regregre", "drama")
        assert (self.film.get_titlu() == "Titanic")
        self.film.set_titlu("Razboiul stelelor")
        assert (self.film.get_titlu() == "Razboiul stelelor")


    def test_get_set_descriere(self):
        self.film = Film(1, "Titanic", "dsufbfer regregre", "drama")
        assert (self.film.get_descriere() == "dsufbfer regregre")
        self.film.set_descriere("ABCDEFG")
        assert (self.film.get_descriere() == "ABCDEFG")


    def test_get_set_gen(self):
        self.film = Film(1, "Titanic", "dsufbfer regregre", "drama")
        assert (self.film.get_gen() == "drama")
        self.film.set_gen("wefdfdfd")
        assert (self.film.get_gen() == "wefdfdfd")


    # def all_teste_filme():
    #     test_get_id()
    #     test_get_set_titlu()
    #     test_get_set_descriere()
    #     test_get_set_gen()
