from problema2.repository.film_repository import IdNotFoundError, DuplicateIdError
from problema2.service.client_service import IsNotCnpError, ClientService
from problema2.service.film_service import FilmService


class IdNotExistError(Exception):
    pass


class IdIsNotIntError:
    pass


class Consola:
    def __init__(self, client_service, film_service):
        self.__client_service = client_service
        self.__film_service = film_service

    def execute_menu(self):
        comenzi = {"c": self.executa_comenzi_client, "f": self.executa_comenzi_film}

        while True:
            c = input( "Alegeti o comanda: pentru a executa functionalitati pe clinti tasteaza c, iar pentru a executa functionalitati pe filme tasteaza f: ")
            if c == "exit":
                print("multumesc ")
                break
            comenzi[c]()

    def executa_comenzi_client(self):
        comenzi = {"adaugare": self.__adaugare_client, "afisare": self.__afisare_client, "sterge": self.__sterge_client,
                   "update": self.__update_client, "help": self.__help_comenzi_client}
        while True:
            print("Alegeti o comanda sau help pentru ajutor(help nume_comanda):", end="\n\t")
            print(*comenzi.keys(), "exit", sep=",")
            cmd, args = self.__citeste_comanda_c()
            if cmd == "exit":
                break
            comenzi[cmd](*args)

    def __citeste_comanda_c(self):
        linie = input()
        poz = linie.find(" ")
        if poz == -1:
            return linie, []
        com = linie[:poz]
        args = linie[poz + 1:]
        args = args.split(",")
        args = [el.strip() for el in args]
        return com, args

    def __help_comenzi_client(self, comanda):
        comenzi = {"adaugare": "adaugare <id>, <nume>, <cnp>", "afisare": "afisare", "sterge": "sterge <id>", "update":"update"}
        print("Utilizare: ", comenzi[comanda])

    def __afisare_client(self):
        all_clients = self.__client_service.get_all_client()
        for client in all_clients:
            print(client)

    def __adaugare_client(self, id, nume, CNP):
        id=int(id)
        CNP=int(CNP)
        try:
            self.__client_service.add_client(id, nume, CNP)
        except IsNotCnpError:
            print("Nu are format de CNP")
        # except DuplicateIdError:
        #     print("Duplicate: id-ul clientului este duplicat")

    def __sterge_client(self):
        self.__afisare_client()
        id = int(input("introdu id-ul: "))
        try:
            self.__client_service.remove_client(id)
        except IdNotExistError:
            print("nu exista acest id")

    def __update_client(self):
        self.__afisare_client()
        id=int(input("introdu id-ul: "))
        nume=input("introdu nume: ")
        CNP=int(input("introdu CNP: "))
        try:
            self.__client_service.modify_client(id, nume, CNP)
        # except IdIsNotIntError:
        #     print("Id nu este de tipul potrivit")
        except IdNotFoundError:
            print("nu exista acest id")
        except IsNotCnpError:
            print("Nu are format de CNP")

    def executa_comenzi_film(self):
        comenzi = {"adaugare": self.__adaugare_film, "afisare": self.__afisare_film, "sterge": self.__sterge_film,
                "update": self.__update_film, "help": self.__help_comenzi_film}
        while True:
            print("Alegeti o comanda sau help pentru ajutor(help nume_comanda):", end="\n\t")
            print(*comenzi.keys(), "exit", sep=",")
            cmd, args = self.__citeste_comanda_f()
            if cmd == "exit":
                break
            comenzi[cmd](*args)

    def __citeste_comanda_f(self):
        linie = input()
        poz = linie.find(" ")
        if poz == -1:
            return linie, []
        com = linie[:poz]
        args = linie[poz + 1:]
        args = args.split(",")
        args = [el.strip() for el in args]
        return com, args

    def __help_comenzi_film(self, comanda):
        comenzi = {"adaugare": "adaugare <id>, <titlu>, <descriere>, <gen>", "afisare": "afisare",
                   "sterge": "sterge ","update": "update"}
        print("Utilizare: ", comenzi[comanda])

    def __afisare_film(self):
        all_movies = self.__film_service.get_all_films()
        for movie in all_movies:
            print(movie)

    def __adaugare_film(self, id, titlu, descriere, gen):
        id=int(id)
        try:
            self.__film_service.add_film(id, titlu, descriere, gen)
        except TypeError:
            print("Nu este de tip int")

    def __sterge_film(self):
        self.__afisare_film()
        id = int(input("introdu id-ul: "))
        try:
            self.__film_service.remove_film(id)
        except IdNotExistError:
            print("nu exista acest id")



    def __update_film(self):
        self.__afisare_film()
        id = int(input("introdu id-ul: "))
        try:
            titlu = input("Introdu titlul: ")
            descriere = input("Introdu descrierea: ")
            gen = input("Introdu genul: ")
            self.__film_service.modify_film(id, titlu, descriere, gen)
        except IdNotFoundError:
            print("nu exista acest id")
