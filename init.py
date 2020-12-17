import persona
import rubrica
import errori
import csv


def menu():
    print("1) Aggiungi un contatto.")
    print("2) Modifica un contatto.")
    print("3) Rimuovi un contatto.")
    print("4) Cerca un contatto.")
    print("5) Stampa elenco contatti.")
    print("6) Esci.")

print("Benvenuto nella tua rubrica")
scelta = 0
lista=[]
rubrica=rubrica.Rubrica(lista)
contatto = persona.Persona


def importContatti():
    try:
        box=[]
        contatoreflag=0
        with open('perimport.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                box.append(row)
            i = 0
            j = 1
            z = 2
            y = 3
            while(True):
                nome=str(box[i]).replace('[','').replace("'","").replace(']','')
                cognome=str(box[j]).replace('[','').replace("'","").replace(']','')
                numero=int(str(box[z]).replace('[','').replace("'","").replace(']',''))
                email=str(box[y]).replace('[', '').replace("'", "").replace(']', '')
                rubrica.addContatto(contatto(nome, cognome ,numero, email))
                contatoreflag=contatoreflag+1
                if(len(box)==contatoreflag*4):
                    break
                else:
                    i += 4
                    j += 4
                    z += 4
                    y += 4
    except Exception as e:
        print("Nessuna lista da importare")

importContatti()
while(scelta != 6):
    menu()

    scelta = int(input("Scegli cosa fare: "))
    if scelta == 1:
        try:
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")
            numero = int(input("Inserisci il numero di telefono: "))
            email = input("Inserisci l'indirizzo email: ")
            rubrica.controlloNumeri(numero)
            rubrica.addContatto(contatto(nome, cognome, numero, email))
            print("Fatto!")
        except errori.ValoreObbligatorio:
            print("Valori obbligatori non immessi, riprovare...")
            print()
        except ValueError as e:
            print("Il numero telefonico non può essere una stringa, riprovare...")
            print()
        except errori.ErroreDuplicato:
            print("Valori duplicati immessi, riprovare...")
            print()


    elif scelta == 2:
         posizione2 = int(input("Inserisci il numero telefonico dell'elemento da modificare: "))
         rubrica.modificaContatto(posizione2)

    elif scelta == 3:
        posizione = int(input("Inserisci il numero telefonico dell'elemento da eliminare: "))
        if rubrica.rimuoviContatto(posizione):
            print("Fatto!")
        else:
            print("Nessun contatto presente con quel numero di telefono")

    elif scelta == 4:
        cercare = input("Inserisci il cognome da cercare: ")
        if rubrica.cercaContatto(cercare):
            print("Fatto!")
        else:
            print("Nessun contatto presente con quel cognome")

    elif scelta == 5:
        rubrica.stampaContatti()
        print("Fatto!")

    else:
        if scelta != 6:
            print("Errore! Riprovare...")
        else:
            rubrica.exportContatti()
            rubrica.exportContattiPerImport()


print("Arrivederci")