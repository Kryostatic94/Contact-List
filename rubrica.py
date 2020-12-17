import persona
import errori
import csv

class Rubrica:
        lista = []
        def __init__(self,lista):
            self.lista=lista


        def addContatto(self,persona):
            self.lista.append(persona)

        def rimuoviContatto(self, numerotelefono):
            for persona.Persona in self.lista:
                if persona.Persona.get_numeroTelefonico() == numerotelefono:
                    self.lista.remove(persona.Persona)
                    return True


        def cercaContatto(self, cognome):
            for persona.Persona in self.lista:
                if persona.Persona.get_Cognome().lower() == cognome.lower():
                    print(persona.Persona)
                    return True

        def stampaContatti(self):
            contatore=1
            for i in self.lista:
                print(f"{contatore}) {i}")
                contatore=contatore+1

        def controlloNumeri(self,numero):
            for persona.Persona in self.lista:
                if persona.Persona.get_numeroTelefonico() == numero:
                    raise errori.ErroreDuplicato
                else:
                    return True

        def modificaContatto(self,numerotelefono):
            for persona.Persona in self.lista:
                if persona.Persona.get_numeroTelefonico() == numerotelefono:
                    try:
                        numero = int(input("Inserisci il numero di telefono: "))
                        self.controlloNumeri(numero)
                        persona.Persona.set_numeroTelefonico(numero)
                        nome = input("Inserisci il nome: ")
                        if nome:
                            persona.Persona.set_Nome(nome)
                        else:
                            raise errori.ValoreObbligatorio
                        cognome = input("Inserisci il cognome: ")
                        if cognome:
                            persona.Persona.set_Cognome(cognome)
                        else:
                            raise errori.ValoreObbligatorio
                        email = input("Inserisci l'indirizzo email: ")
                        if email:
                            persona.Persona.set_Email(email)
                        else:
                            raise errori.ValoreObbligatorio
                        print("Fatto!")
                    except errori.ValoreObbligatorio:
                        print("Valori obbligatori non immessi, riprovare...")
                        print()
                        return
                    except ValueError as e:
                        print("Il numero telefonico non può essere una stringa, riprovare...")
                        print()
                        return
                    except errori.ErroreDuplicato:
                        print("Valori duplicati non immessi, riprovare...")
                        print()
                        return

        def exportContatti(self):
            try:
                file_output = csv.writer(open("lista.csv", "w", newline=''))
                for i in range(len(self.lista)):
                    file_output.writerow([str(self.lista[i])])
            except Exception as e:
                print(e)


        def exportContattiPerImport(self):
            try:
                file_output = csv.writer(open("perimport.csv", "w", newline=''))
                for i in range(len(self.lista)):
                    file_output.writerow([str(self.lista[i].get_Nome())])
                    file_output.writerow([str(self.lista[i].get_Cognome())])
                    file_output.writerow([str(self.lista[i].get_numeroTelefonico())])
                    file_output.writerow([str(self.lista[i].get_Email())])
            except Exception as e:
                print(e)














