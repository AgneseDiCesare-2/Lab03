import spellchecker
import time

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
        file="resources/Italian.txt"
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        start = time.time()  # inizio misurazione
        errori=sc.handleSentence(txtIn,file)
        end = time.time()  # fine misurazione
        print("Parole errate:")
        for e in errori:
            print(e)
        print("Time elapsed:", end - start, "seconds")
        continue

    elif int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        file="resources/English.txt"
        txtIn = input() #scrivo la frase
        start = time.time()  # inizio misurazione
        errori = sc.handleSentence(txtIn, file)
        end = time.time()  # fine misurazione
        print("Parole errate:")
        for e in errori:
            print(e)
        continue

    elif int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        file="resources/Spanish.txt"
        txtIn = input()
        start = time.time()  # inizio misurazione
        errori = sc.handleSentence(txtIn, file)
        end = time.time()  # fine misurazione
        print("Parole errate:")
        for e in errori:
            print(e)
        continue

    elif int(txtIn) == 4:
        break


