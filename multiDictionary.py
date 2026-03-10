from dictionary import Dictionary
from richWord import RichWord

class MultiDictionary:
    def __init__(self):
       self._dict=Dictionary()

    def printDic(self, language):
        return self._dictonary.loadDictonary(path)

    def searchWord(self, testo, path): #
        parole_dizionario = self.printDic(path)
        listaRichWord = []
        paroleInserite = testo.split().strip()
        for word in paroleInserite:
            corretta = word.lower() in parole_dizionario
            nuova = RichWord(word, corretta)
            listaRichWord.append(nuova)

        return listaRichWord


