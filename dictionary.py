from fileinput import filename

class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path): #apre il dizionario che gli passo in input
        with open(path, "r", encoding="utf-8") as f:
            self._dict=[riga.strip() for riga in f.readlines()]
        return self._dict

    def printAll(self):
        for parola in self._dict:
            print(parola)

    @property
    def dict(self):
        return self._dict