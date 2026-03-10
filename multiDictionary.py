from dictionary import Dictionary
from richWord import RichWord

class MultiDictionary:
    def __init__(self):
       self._dict=Dictionary() #L'OGGETTO MULTIDICTIONARY CONTIENE UN ALTRO OGGETTO (DICTIONARY)

    def printDic(self, path):
        return self._dict.loadDictionary(path)

    def searchWord(self, testo, path): #
        parole_dizionario = self.printDic(path)
        listaRichWord = []
        paroleInserite = testo.split()
        for word in paroleInserite:
            corretta = word.lower() in parole_dizionario
            nuova = RichWord(word, corretta)
            listaRichWord.append(nuova)

        return listaRichWord


