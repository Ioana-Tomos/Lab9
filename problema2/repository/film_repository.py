from domain.validators import DuplicateIdError, IdNotFoundError


class FilmRepository():
    def __init__(self, validator):
        self.__all_films={}
        self.__validator=validator

    def find_all(self):
        return list(self.__all_films.values())

    def save(self, film):
        self.__validator.validate(film)
        if self.find_by_id(int(film.id)) is not None:
            raise DuplicateIdError("Id-ul este dulicat")
        self.__all_films[film.id]=film

    def update(self,film):
        self.__validator.validate(film)
        if self.find_by_id(film.id) is None:
            raise IdNotFoundError("Id-ul nu exista")
        self.__all_films[film.id]=film

    def delete_by_id(self,id):
        if self.find_by_id(id) is None:
            raise IdNotFoundError("Id-ul nu exista")
        self.__all_films.pop(id)

    def find_by_id(self, id_f):
        for film in self.__all_films.values():
            if film.id==id_f:
                return id_f
        return None