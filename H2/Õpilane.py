from H2.Kodutöö import Kodutöö

class Õpilane:
    def __init__(self, täisNimi, kursuseNimietus):
        self.nimi = täisNimi
        self.kursus = kursuseNimietus
        self.tegemataKodutööd = [] #Tühi list
        self.tehtudKodutööd = []

    def lisaKodutöö(self, lisatavKodutöö):
        self.tegemataKodutööd.append(lisatavKodutöö)

    def tagastaTegemataKodutööd(self):
        for uuritavKodutöö in self.tegemataKodutööd:
            print(uuritavKodutöö.pealkiri)

    def märgiKodutööTehtud(self, kodutöö):
        kodutöö.kasTehtud = True
        self.tegemataKodutööd.remove(kodutöö)
        self.tehtudKodutööd.append(kodutöö)

    def tagastaTehtudKodutööd(self):
        for tehtudKodutöö in self.tehtudKodutööd:
            print(tehtudKodutöö.pealkiri)

    def tagastaHindelisedKodutööd(self):
        for uuritavKodutöö in self. tegemataKodutööd:
            if uuritavKodutöö.kasHindeline == True:
                print(uuritavKodutöö.pealkiri)
Õpilane1 = Õpilane('Joosep Joosepson', 'ABC21')
kodutöö1 = Kodutöö('Esse mingil teemal')