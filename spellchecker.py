import time
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        #deve fornire l'output per il main
        paroleErrate=list()
        lista=md.searchWord(self, txtIn, language)
        for parola in lista:
            if parola.corretta==True:
                continue
            else:
                paroleErrate.append(parola)
        print(paroleErrate)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    pass