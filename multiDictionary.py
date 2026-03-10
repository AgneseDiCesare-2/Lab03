import dictionary as d
import richWord as rw
from main import txtIn, file

listaRichWord=list()

class MultiDictionary:
    def __init__(self):
       pass

    def printDic(self, language):
        return d.loadDictonary(file)
        #restituisce una lista di parole

    def searchWord(self, testo, language): #
        wordsEsistenti=self.printDic(language) #tutte le parole che esistono nella lingua
        paroleInserite=testo.split().strip()
        for word in paroleInserite:
            nuova=RichWord(word)
            listaRichWord.append(nuova) #PRIMA DEVO ASSICURARMI CHE IL VALORE BOOLEANO VENGA IMPOSTATO, COSI' DOVREBBE
        return listaRichWord


