import errori

class Persona:
    def __init__(self, nome, cognome, numeroTelefonico, email):
        if nome:
            self.__nome = nome
        else:
            raise errori.ValoreObbligatorio
        if cognome:
            self.__cognome = cognome
        else:
            raise errori.ValoreObbligatorio
        if numeroTelefonico:
            self.__numeroTelefonico = numeroTelefonico
        else:
            raise errori.ValoreObbligatorio
        if email:
            self.__email = email
        else:
            self.__email = "Non specificato"

    def get_Email(self):
        return self.__email

    def set_Email(self, email):
        self.__email = email

    def get_Nome(self):
        return self.__nome

    def set_Nome(self, nome):
        self.__nome = nome

    def get_Cognome(self):
        return self.__cognome

    def set_Cognome(self, cognome):
        self.__cognome = cognome

    def get_numeroTelefonico(self):
        return self.__numeroTelefonico

    def set_numeroTelefonico(self, numeroTelefonico):
        self.__numeroTelefonico = numeroTelefonico



    def __str__(self):
        return f"Nome: {self.__nome} ,Cognome: {self.__cognome} ,Numero di telefono: {self.__numeroTelefonico} ,Email: {self.__email} "
