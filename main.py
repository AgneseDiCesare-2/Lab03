import spellchecker

sc = spellchecker.SpellChecker()
file=None
while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!
    if (txtIn) not in [1,2,3,4]:
        print("Errore, inserisci un numero da 1 a 4!")
        continue

    if int(txtIn) == 1:
        file="italian.txt"
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        file="English.txt"
        txtIn = input() #scrivo la frase
        sc.handleSentence(txtIn,"english")

        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        file="Spanish.txt"
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")
        continue

    if int(txtIn) == 4:
        break


