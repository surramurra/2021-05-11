from Hindeline.Raamat import Raamat

class Külastaja:
    def __init__(self,eesNimi,perekonnaNimi):
        self.eesnimi = eesNimi
        self.perenimi = perekonnaNimi
        self.laenutatudRaamatud = []

    def laenutaRaamat(self,Raamat):
        if not Raamat.laenutatud:
            Raamat.laenutatud = True
            self.laenutatudRaamatud.append(Raamat)
        else:
            print("Raamatut ei saa laenutada, see on juba välja laenutatud!")

    def tagastaRaamat(self, Raamat):
        if Raamat in self.laenutatudRaamatud:
            Raamat.laenutatud = False
            self.laenutatudRaamatud.remove(Raamat)
        else:
            print("Te pole seda raamatud laenanud.")

    def  kuvaLaenutatudRaamatud(self):
        if self.laenutatudRaamatud:
            for raamat in self.laenutatudRaamatud:
                print(raamat.tiitel)
        else:
            print('Vabandame, hetkel pole laenutatud raamatuid!!!')

Külastaja1 = Külastaja('Joosep','Joosepson')
Raamat1 = Raamat('Mingi vahva raamat','Keegi kaval autor', 305)
Raamat2 = Raamat('Parimad koka road','Kuulus Ekspert', 275)

Külastaja1.laenutaRaamat(Raamat1)
Külastaja1.laenutaRaamat(Raamat2)

Külastaja1.tagastaRaamat(Raamat1)
Külastaja1.laenutaRaamat(Raamat2)
Külastaja1.tagastaRaamat(Raamat1)
Külastaja1.kuvaLaenutatudRaamatud()