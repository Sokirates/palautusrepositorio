class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.edellinen_arvo = 0

    def miinus(self, operandi):
        self.edellinen_arvo = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.edellinen_arvo = self._arvo
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def kumoa(self):
        self._arvo = self.edellinen_arvo

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
