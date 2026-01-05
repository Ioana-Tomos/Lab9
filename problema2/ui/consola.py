from domain.validators import IsNotCnpError, IdNotFoundError, DuplicateIdError


class IdNotExistError(Exception):
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
                print("multumesc! <3 ")
                break
            try:
                comenzi[c]()
            except KeyError:
                print("Comanda nu a fost introdusa corect ")

    def executa_comenzi_client(self):
        comenzi = {"adaugare": self.__adaugare_client, "afisare": self.__afisare_client, "sterge": self.__sterge_client,
                   "update": self.__update_client, "help": self.__help_comenzi_client}
        while True:
            print("Alegeti o comanda sau help pentru ajutor(help nume_comanda):", end="\n\t")
            print(*comenzi.keys(), "exit", sep=",")
            cmd, args = self.__citeste_comanda_c()
            if cmd == "exit":
                break
            try:
                comenzi[cmd](*args)
            except KeyError:
                print("Comanda nu a fost introdusa corect.  Pentru a afla forma corecta intrdouceti:help <numele comenzii>  ")
            except TypeError:
                print("Comanda nu a fost introdusa corect.  Pentru a afla forma corecta intrdouceti:help <numele comenzii>  ")

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
        comenzi = {"adaugare": "adaugare <id>, <nume>, <cnp>", "afisare": "afisare", "sterge": "sterge", "update":"update"}
        print("Utilizare: ", comenzi[comanda])

    def __afisare_client(self):
        all_clients = self.__client_service.get_all_client()
        for client in all_clients:
            print(client)

    def __adaugare_client(self, id, nume, CNP):

        try:
            id=int(id)
            CNP=int(CNP)
            self.__client_service.add_client(id, nume, CNP)
        except IsNotCnpError:
            print("Nu are format de CNP")
        except DuplicateIdError:
            print("Duplicate: id-ul clientului este duplicat")
        except ValueError:
            print("Id-ul si CNP-ul trebuie sa fie numere")

    def __sterge_client(self):
        self.__afisare_client()
        try:
            id = int(input("introdu id-ul: "))
            self.__client_service.remove_client(id)
        except IdNotExistError as m:
            print(m)
        except ValueError:
            print("Id-ul trebuie sa fie numar")

    def __update_client(self):
        self.__afisare_client()
        try:
            id=int(input("introdu id-ul: "))
            nume=input("introdu nume: ")
            CNP=int(input("introdu CNP: "))
            self.__client_service.modify_client(id, nume, CNP)

        except IdNotFoundError:
            print("nu exista acest id")
        except IsNotCnpError:
            print("Nu are format de CNP")
        except ValueError:
            print("Id-ul si CNP-ul trebuie sa fie numere")

    def executa_comenzi_film(self):
        comenzi = {"adaugare": self.__adaugare_film, "afisare": self.__afisare_film, "sterge": self.__sterge_film,
                "update": self.__update_film, "help": self.__help_comenzi_film}
        while True:
            print("Alegeti o comanda sau help pentru ajutor(help nume_comanda):", end="\n\t")
            print(*comenzi.keys(), "exit", sep=",")
            cmd, args = self.__citeste_comanda_f()
            if cmd == "exit":
                break
            try:
                comenzi[cmd](*args)
            except KeyError:
                print("Comanda nu a fost introdusa corect. Pentru a afla forma corecta intrdouceti:help <numele comenzii> ")
            except TypeError:
                print("Comanda nu a fost introdusa corect. Pentru a afla forma corecta intrdouceti:help <numele comenzii> ")


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
        try:
            id=int(id)
            self.__film_service.add_film(id, titlu, descriere, gen)
        except TypeError:
            print("Nu este de tip int")
        except ValueError:
            print("Id-ul trebuie sa fie de tip int")

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
