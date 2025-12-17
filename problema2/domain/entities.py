
class BaseEntity():
    def __init__(self, id):
        self.__id = id
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    def __str__(self):
        return "BaseEntity: {" +"id="+ str(self.__id)+ " }"

class Client(BaseEntity):
    def __init__(self, id, nume, CNP):
        super().__init__(id)
        self.__nume = nume
        self.__CNP = CNP

    # def get_id(self):
    #     return self.__id
    @property
    def nume(self):
        return self.__nume
    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def CNP(self):
        return self.__CNP

    @CNP.setter
    def CNP(self, val):
        self.__CNP = val

    def __str__(self):
        return "Client: " + super().__str__() + ", " + self.__nume + ", " + str(self.__CNP)


class Film(BaseEntity):
    def __init__(self, id, titlu, descriere, gen):
        super().__init__(id)
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    @property
    def titlu(self):
        return self.__titlu
    @titlu.setter
    def titlu(self, value):
        self.__titlu = value

    @property
    def descriere(self):
        return self.__descriere
    @descriere.setter
    def set_descriere(self, value):
        self.__descriere = value

    @property
    def gen(self):
        return self.__gen

    @gen.setter
    def gen(self, value):
        self.__gen = value

    def __str__(self):
        return "Film: "+super().__str__()+", "+self.__titlu+", "+self.__descriere+", "+self.__gen

