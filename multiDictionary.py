from selectors import SelectSelector

from dictionary import Dictionary
from richWord import RichWord

class MultiDictionary:
    def __init__(self):
       self._dict=Dictionary() #L'OGGETTO MULTIDICTIONARY CONTIENE UN ALTRO OGGETTO (DICTIONARY)

    def printDic(self, path):
        return self._dict.loadDictionary(path)

    def searchWord(self, testo, path):
        parole_dizionario = self.printDic(path)
        listaRichWord = []

        paroleInserite = testo.split()

        for word in paroleInserite:
            word_pulita = word.lower().strip(".,;:!?")
            if parole_dizionario.__contains__(word_pulita):
                corretta = True
            else:
                corretta = False

            nuova = RichWord(word, corretta)
            listaRichWord.append(nuova)

        return listaRichWord

    def searchWordLinear(self, testo, path):
        parole_dizionario = self.printDic(path)
        listaRichWord = []

        paroleInserite = testo.split()

        for word in paroleInserite:
            corretta=False
            word_pulita = word.lower().strip(".,;:!?")
            for parola in parole_dizionario:
                if (word_pulita == parola): #IMPLEMENTA __eq__ !
                    corretta = True

            nuova = RichWord(word, corretta)
            listaRichWord.append(nuova)

        return listaRichWord
