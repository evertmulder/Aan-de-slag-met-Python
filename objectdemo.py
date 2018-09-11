class Doos:
    def __init__(self, breedte, hoogte, diepte):
        self.breedte = breedte
        self.hoogte = hoogte
        self.diepte = diepte
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
print(verhuisdoos)
verhuisdoos.plaklabel("Huiskamer")
print(verhuisdoos)

verhuisdozen = []
verhuisdozen.append(verhuisdoos)
