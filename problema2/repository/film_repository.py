class DuplicateIdError(Exception):
    pass
class IdNotFoundError(Exception):
    pass

class FilmRepository():
    def __init__(self):
        self.__all_films={}

    def find_all(self):
        return list(self.__all_films.values())

    def save(self, film):
        if self.find_by_id(film.get_id()) is not None:
            raise DuplicateIdError("Id-ul este dulicat")
        self.__all_films[film.get_id()]=film

    def update(self,film):
        if self.find_by_id(film.get_id()) is None:
            raise IdNotFoundError("Id-ul nu exista")
        self.__all_films[film.get_id()]=film

    def delete_by_id(self,id):
        if self.find_by_id(id) is None:
            raise IdNotFoundError("Id-ul nu exista")
        self.__all_films.pop(id)

    def find_by_id(self, id_f):
        for film in self.__all_films.values():
            if film.get_id()==id_f:
                return id_f
        return None