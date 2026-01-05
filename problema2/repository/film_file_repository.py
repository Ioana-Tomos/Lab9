from domain.entities import Film
from domain.validators import DuplicateIdError, IdNotFoundError
from repository.film_repository import FilmRepository


class FilmFileRepository(FilmRepository):

    def __init__(self, validator, filename):
        super().__init__(validator)
        self.__filename = filename
        self.__load_data()

    def __load_data(self):
        with open(self.__filename) as f:
            for linie in f:
                lista_film = linie.split(",")
                try:
                    film = Film(int(lista_film[0]), lista_film[1], lista_film[2], lista_film[3].strip())
                    super().save(film)
                except ValueError:
                    print("\n"+"!!!!!!!!!!!!!!Gresala in fisierul filme!!!!!!!!!!!!!!!!!!"+"\n")
                except DuplicateIdError:
                    print("\n"+"!!!!!!!!!!!!!!Id duplicat in fisierul filme!!!!!!!!!!!!!!!!!!"+"\n")


    def save(self, film):
        super().save(film)
        try:
            self.__add_to_file(film)
        except DuplicateIdError as e:
            print(e)

    def __add_to_file(self, film):
        with open(self.__filename, "a") as f:
            string_film = str(film.id) + "," + film.titlu + "," + film.descriere + "," + film.gen
            f.write(string_film)

    def update(self, film):
        super().update(film)
        try:
            self.__rewrite()
        except IdNotFoundError:
            print("acest id nu este in lista")
        # self.__rewrite()


    def delete_by_id(self, id):
        try:
            super().delete_by_id(id)
        except IdNotFoundError as e:
            print(e)
        self.__rewrite()

    def __rewrite(self):
        lista_filme = self.find_all()
        with open(self.__filename, "w") as f:
            for film in lista_filme:
                film_file = str(film.id) + "," + str(film.titlu) + "," + str(film.descriere) +","+ str(film.gen)+"\n"
                f.write(film_file)

