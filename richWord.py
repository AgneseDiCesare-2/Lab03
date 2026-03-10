from multiDictionary import MultiDictionary as md
from main import txtIn, file

dictionaryRif = md.printDic(file)

class RichWord:
    def __init__(self, parola):
        self._parola = parola
        self._corretta = dictionaryRif.contains(parola) #TRUE SE LA CONTIENE, FALSE ALTRIMENTI

    @property
    def corretta(self):
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        self._corretta = boolValue

    def __str__(self):
        return self._parola