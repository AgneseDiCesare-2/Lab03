
class RichWord:
    def __init__(self, parola, corretta=None):
        self.parola = parola
        self._corretta = corretta

    @property
    def corretta(self):
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        self._corretta = boolValue

    def __str__(self):
        return self._parola