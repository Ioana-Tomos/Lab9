import unittest

from problema2.domain.film import Film
from problema2.repository.film_repository import FilmRepository, DuplicateIdError

class FilmRepoTestCase(unittest.TestCase):
    def test_save(self):
        film = Film(1,"Titanic","film romantic","romance")
        self.film_repo=FilmRepository()
        assert (len(self.film_repo.find_all())==0)
        self.film_repo.save(film)
        assert (len(self.film_repo.find_all())==1)
        assert (self.film_repo.find_all()[0].get_id()==film.get_id())
        assert (self.film_repo.find_all()[0].get_titlu()==film.get_titlu())
        assert (self.film_repo.find_all()[0].get_descriere()==film.get_descriere())
        assert (self.film_repo.find_all()[0].get_gen()==film.get_gen())
        try:
            self.film_repo.save(film)
            assert False
        except DuplicateIdError:
            assert True

    def test_find_all(self):
        film = Film(1, "Titanic", "film romantic", "romance")
        self.film_repo = FilmRepository()
        assert (isinstance(self.film_repo.find_all(), list))
        assert (len(self.film_repo.find_all()) == 0)
        self.film_repo.save(film)
        assert (self.film_repo.find_all()[0].get_id() == film.get_id())
        assert (self.film_repo.find_all()[0].get_titlu() == film.get_titlu())
        assert (self.film_repo.find_all()[0].get_descriere() == film.get_descriere())
        assert (self.film_repo.find_all()[0].get_gen() == film.get_gen())

    def test_update(self):
        self.film_repo = FilmRepository()
        film1 = Film(1, "Titanic", "film romantic", "romance")
        film2 = Film(2, "Fast&Furios", "film de actiune", "actiune")
        self.film_repo.save(film1)
        assert (self.film_repo.find_all()[0].get_id() == film1.get_id())
        assert (self.film_repo.find_all()[0].get_titlu() == film1.get_titlu())
        assert (self.film_repo.find_all()[0].get_descriere() == film1.get_descriere())
        assert (self.film_repo.find_all()[0].get_gen() == film1.get_gen())
        self.film_repo.update(film2)
        assert (self.film_repo.find_all()[0].get_id() == film2.get_id())
        assert (self.film_repo.find_all()[0].get_titlu() == film2.get_titlu())
        assert (self.film_repo.find_all()[0].get_descriere() == film2.get_descriere())
        assert (self.film_repo.find_all()[0].get_gen() == film2.get_gen())

    def test_delete_by_id(self):
        film1 = Film(1, "Titanic", "film romantic", "romance")
        film2= Film(2, "Fast&Furios", "film de actiune", "actiune")
        self.film_repo = FilmRepository()
        self.film_repo.save(film1)
        self.film_repo.save(film2)
        self.film_repo.delete_by_id((film1.get_id()))
        assert (self.film_repo.find_all()[0].get_id() == film2.get_id())
        assert (self.film_repo.find_all()[0].get_titlu() == film2.get_titlu())
        assert (self.film_repo.find_all()[0].get_descriere() == film2.get_descriere())
        assert (self.film_repo.find_all()[0].get_gen() == film2.get_gen())

    # def test_all_film_repository():
    #     test_save()
    #     test_find_all()
    #     test_update()
    #     test_delete_by_id()
