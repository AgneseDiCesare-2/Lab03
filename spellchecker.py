
from multiDictionary import MultiDictionary
class SpellChecker:
    def __init__(self):
        self._multiDictionary = MultiDictionary()

    def handleSentence(self, txtIn, path):
        #deve fornire l'output per il main
        print("-"*32)
        print("Using Contains: ")
        paroleErrate=list()
        lista=self._multiDictionary.searchWord(txtIn, path)
        for parola in lista:
            if not parola.corretta:
                paroleErrate.append(parola)
        return paroleErrate

    def handleSentenceLinear(self, txtIn, path):
        print("-" * 32)
        print("Using Linear Research: ")
        paroleErrate = list()
        lista = self._multiDictionary.searchWordLinear(txtIn, path)
        for parola in lista:
            if not parola.corretta:
                paroleErrate.append(parola)
        return paroleErrate

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