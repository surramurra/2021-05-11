from H1.Toit import Toit

class Menüü:
    def __init__(self, pealkiri):
        self.pealkiri = pealkiri
        self.toidud = []

    def lisaToit(self, toit):
        self.toidud.append(toit)
    def kuvaToidudJaHinnad(self):
        for uusToit in self.toidud:
            print(uusToit.nimetus, uusToit.hind, uusToit.päevaEri)
    def kuvaPäevaEri(self):
        for uuritavToit in self.toidud:
            if uuritavToit.päevaEri == True:
                print('Päevaeripakkumine on: ' ,uuritavToit.nimetus, uuritavToit.hind)


    def leiaKallimToit(self):
        maxHind = 0
        for Toit in self.toidud:
            if Toit.hind >= maxHind:
                maxHind = Toit.hind
                kalleimToit = Toit
        print("Kallim toit on: ",kalleimToit.nimetus, kalleimToit.hind)


uusToit = Toit('Seapraad', 3.5, False)
salvestaMenüü = Menüü('Al a carte')

salvestaMenüü.lisaToit(uusToit)

print(uusToit.nimetus, uusToit.hind, uusToit.päevaEri)
print(salvestaMenüü.toidud)
print(salvestaMenüü.toidud[0].nimetus)

toit2 = Toit('Kapsapraad', 4, True)
salvestaMenüü.lisaToit(toit2)

salvestaMenüü.kuvaPäevaEri()
salvestaMenüü.leiaKallimToit()