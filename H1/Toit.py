class Toit:
    def __init__(self, nimetus, roaHind, päevaEri):
        self.nimetus = nimetus
        self.hind = roaHind
        self.päevaEri = päevaEri

uusToit = Toit('Seapraad', 3, False)
print(uusToit.nimetus, uusToit.hind, uusToit.päevaEri)