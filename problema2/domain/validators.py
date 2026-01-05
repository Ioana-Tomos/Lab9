from abc import abstractmethod


class IdNotFoundError(Exception):
    pass

class DuplicateIdError(Exception):
    pass

class IsNotCnpError(Exception):
    pass

class IdIncorectError(Exception):
    pass


class EntityValidator:
    @abstractmethod
    def validate(self, entity):
        if entity.id<0:
            raise IdIncorectError("Id-ul este negativ")

class ClientValidator(EntityValidator):
    def validate(self, person):
        super().validate(person)
        if len(str(person.CNP))!=13:
            raise IsNotCnpError("Forma cnp-ului nu este corecta")

class FilmValidator(EntityValidator):
    def validate(self, film):
        super().validate(film)

