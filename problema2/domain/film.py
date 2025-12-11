from problema2.domain.base_entety import BaseEntity


class Film(BaseEntity):
    def __init__(self, id, titlu, descriere, gen):
        super().__init__(id)
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen



    # def get_id(self):
    #     return self.__id

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_gen(self):
        return self.__gen

    # def set_id(self, id):
    #     self.__id = id

    def set_titlu(self, titlu):
        self.__titlu = titlu

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_gen(self, gen):
        self.__gen = gen

    def __str__(self):
        return "Film: "+super().__str__()+", "+self.__titlu+", "+self.__descriere+", "+self.__gen

