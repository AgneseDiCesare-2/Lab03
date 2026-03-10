import spellchecker

sc = spellchecker.SpellChecker()
file=None

while(True):
    sc.printMenu()
    txtIn = input()
    # Add input control here!
    if (txtIn) not in ["1","2","3","4"]:
        print("Errore, inserisci un numero da 1 a 4!")
        continue

    if int(txtIn) == 1:
        file="resources/italian.txt"
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        errori=sc.handleSentence(txtIn,file)
        print("Parole errate:", [str(p) for p in errori])

    elif int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        file="resources/English.txt"
        txtIn = input() #scrivo la frase
        errori = sc.handleSentence(txtIn, file)
        print("Parole errate:", [str(p) for p in errori])

        continue

    elif int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        file="resources/Spanish.txt"
        txtIn = input()
        errori = sc.handleSentence(txtIn, file)
        print("Parole errate:", [str(p) for p in errori])

    elif int(txtIn) == 4:
        break


