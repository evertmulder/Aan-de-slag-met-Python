class Kubus:
    def __init__(self, breedte, hoogte, diepte):
        self.breedte = breedte
        self.hoogte = hoogte
        self.diepte = diepte

    def __str__(self):
        print("Dit is een kubus")


class Doos(Kubus):
    def __init__(self, breedte, hoogte, diepte):
        super().__init__(breedte, hoogte, diepte)
        self.label = None
        self.isOpen = True

    def __str__(self):
        if self.label is not None:
            return "Het label op deze doos zegt '" + self.label + "'"
        else:
            return "Er zit geen label op deze doos"

    def plaklabel(self, tekst):
        self.label = tekst

    def sluit(self, doeDicht):
        if doeDicht:
            self.isOpen = False
        else:
            self.isOpen = True

verhuisdoos = Doos(30, 30, 30)
verhuisdoos.sluit(True)
