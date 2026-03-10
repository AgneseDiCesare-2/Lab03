from fileinput import filename

class Dictionary:
    def __init__(self):
        pass

    def loadDictionary(self,path): #apre il dizionario che gli passo in input
        parole = list()  # parole memorizzate: lista al momento vuota
        with open(path, "r", encoding="utf-8") as f:
            righe=f.readlines()
            for parola in righe:
                parole.append(parola.strip())
        return parole

    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict