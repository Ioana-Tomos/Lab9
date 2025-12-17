class IdNotFoundCError(Exception):
    pass

class DuplicateIdError(Exception):
    pass

class IsNotCnpError(Exception):
    pass

class IdIncorectError(Exception):
    pass

class ClientValidator:
    def validateclient(self, person):
        if len(str(person.get_cnp))!=13:
            raise IsNotCnpError("Forma cnp-ului nu este corecta")

        if person.get_id<0:
            raise IdIncorectError("Id-ul este negativ")
class FilmValidator:
    def validatefilm(self, film):
        pass
