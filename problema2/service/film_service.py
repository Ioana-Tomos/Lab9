from problema2.domain.film import Film

class DuplicateIdError(Exception):
    pass
class IdNotFoundError(Exception):
    pass


class FilmService:
    def __init__(self,film_repository):
        self.__film_repository=film_repository

    def add_film(self,id,titlu,descriere,gen):
        id=int(id)
        film=Film(id,titlu,descriere,gen)
        try:
            self.__film_repository.save(film)
        except DuplicateIdError:
            print("Duplicate:id-ul filmului este duplicat")

    def remove_film(self,id):
        self.__film_repository.delete_by_id(id)

    def get_all_films(self):
        return self.__film_repository.find_all()

    def modify_film(self,id,titlu,descriere,gen):
        film_existent=self.__film_repository.find_by_id(id)
        if film_existent is None:
            raise IdNotFoundError("Nu a gasit acest id")
        film=Film(id,titlu,descriere,gen)
        self.__film_repository.update(film)

    def find_by_id(self,id):
        return self.__film_repository.find_by_id(id)


