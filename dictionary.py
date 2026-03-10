from fileinput import filename

class Dictionary:
    def __init__(self):
        self._dict = [] #LA CLASSE DICTONARY E' DEFINITA COME UNA LISTA

    def loadDictionary(self,path): #apre il dizionario che gli passo in input
        with open(path, "r", encoding="utf-8") as f:
            self._dict = []
            for riga in f.readlines():
                parola = riga.strip()
                self._dict.append(parola)
        return self._dict #ALLA FINE RESTITUISCE UNA LISTA CON TUTTE LE PAROLE

    def printAll(self):
        for parola in self._dict:
            print(parola)

    @property
    def dict(self):
        return self._dict