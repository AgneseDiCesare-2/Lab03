from operator import truediv
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
                if (word_pulita == parola): #non serve implementare __eq__ perchè sono stringhe
                    corretta = True

            nuova = RichWord(word, corretta)
            listaRichWord.append(nuova)

        return listaRichWord

    def searchWordDiacotonic(self, testo, path):
        dizionario_base= self.printDic(path)
        listaRichWord = []
        paroleInserite = testo.split()

        for word in paroleInserite:
            word_pulita = word.lower().strip(".,;:!?")
            parole_dizionario=dizionario_base[:] #per ogni parola riutilizzo una copia del dizionario intero
            corretta=False
            itera=True

            while itera:
                lunghezza=len(parole_dizionario)
                if lunghezza == 0: #parola non trovata
                    itera = False
                    break

                indiceMeta=int(lunghezza/2)
                parolaMeta=(parole_dizionario.__getitem__( indiceMeta))
                if (parolaMeta>word_pulita): #es. sto cercando "anatra", ma a metà mi fermo su "gatto"
                    parole_dizionario=parole_dizionario[:indiceMeta] #seleziono la prima metà degli elementi
                    continue
                elif (parolaMeta<word_pulita):
                    parole_dizionario = parole_dizionario[indiceMeta + 1:] #seleziono la seconda metà
                    continue
                else: #(parolaMeta==word_pulita)
                    corretta=True
                    itera=False

            nuova = RichWord(word, corretta)
            listaRichWord.append(nuova)

        return listaRichWord




