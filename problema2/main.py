import os

from problema2.repository.client_file_repository import ClientFileRepository
from problema2.repository.film_file_repository import FilmFileRepository
from problema2.service.client_service import ClientService
from problema2.service.film_service import FilmService
from problema2.ui.consola import Consola


# print("Hello lume")


def main():

    print(os.getcwd())
    client_repository = ClientFileRepository('../data/clienti')
    film_repository = FilmFileRepository("../data/filme")
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


