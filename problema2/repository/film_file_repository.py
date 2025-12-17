from domain.entities import Film
from problema2.repository.film_repository import FilmRepository


class FilmFileRepository(FilmRepository):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.__load_data()

    def __load_data(self):
        with open(self.filename) as f:
            for linie in f:
                lista_filme= linie.split(",")
                film=Film(int(lista_filme[0]), lista_filme[1], lista_filme[2], lista_filme[3])
                super().save(film)

    def save(self, film):
        super().save(film)
        self.__add_to_file(film)

    def __add_to_file(self,film):
        with open(self.filename, "a") as f:
            string_film= "\n"+str(film.id)+","+film.titlu+","+film.descriere+","+film.gen
            f.write(string_film)

#todo: stergere,modificare,delete