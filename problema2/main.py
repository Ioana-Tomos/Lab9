import os

from domain.validators import FilmValidator, ClientValidator
from repository.client_file_repository import ClientFileRepository
from repository.film_file_repository import FilmFileRepository
from service.client_service import ClientService
from service.film_service import FilmService
from ui.consola import Consola


# print("Hello lume")


def main():

    print(os.getcwd())
    client_validator=ClientValidator()
    film_validator=FilmValidator()
    client_repository = ClientFileRepository(client_validator,'../data/clienti')
    film_repository = FilmFileRepository(film_validator,'../data/filme')
    client_service = ClientService(client_repository)
    film_service = FilmService(film_repository)
    sc = Consola(client_service, film_service)
    sc.execute_menu()


main()

# def main():
#     print(os.getcwd())
#     student_repository = StudentFileRepository("../../../data/students")
#     student_service = StudentService(student_repository)
#     sc = StudentConsole(student_service)
#     # sc.executa_meniu()
#     sc.executa_comenzi()



#THE BIGGEST MODIFICATION EVER


