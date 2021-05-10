# Ülesanne 2

### ÜL 2.1
Looge PyCharmis 2 faili:

- Kodutöö.py
- Õpilane.py

### ÜL 2.2
Kodutöö.py failis kirjeldage klass Kodutöö ja selle init meetod, millel on vähemalt järgmised omadused:
- **pealkiri**, kus hoiame kodutöö pealkirja.
- **hindeline**, kus hoiame True või False väärtust, kas kodutöö on hindeline.
- **tehtud**, kus hoiame True või False väärtust, kas kodutöö on tehtud. Vaikimisi on see False.

NB: Kõik nende parameetrite väärtused (välja arvatud tehtud) peavad olema sisse antavad sisend parameetriga init meetodis.

### ÜL 2.3
Õpilane.py failis kirjeldage klass Õpilane ja selle init meetod, millel on vähemalt järgmised omadused:
- **nimi**, kus hoiame õpilase täis nime.
- **kuruseNimetus**, kus hoiame õpilase kursuse nimetust.
- **tegemataKodutööd**, tühi list kuhu tulevikus lisame antud kodutöid.
- **tehtudKodutööd**, tühi list kuhu tulevikus lisame tehtud kodutöid.

NB: Kõik nende parameetrite väärtused (välja arvatud tegemataKodutööd ja tehtudKodutööd) peavad olema sisse antavad sisend parameetriga init meetodis.

### ÜL 2.4

Looge klassis Õpilane funktsioon lisaKodutöö(self), mis teeb järgmist:
- Võtab sisend parameetriks Kodutöö objekti
- Lisab selle tegemataKodutööd listi.

### ÜL 2.5

Looge klassis Õpilane funktsioon tagastaTegemataKodutööd(self), mis teeb järgmist:
- Käib tsükliga läbi tegemataKodutööd listi ning prindib iga kodutöö pealkiri omaduse.

### ÜL 2.6

Looge klassis Õpilane funktsioon märgiKodutööTehtud(self), mis teeb järgmist:
- Võtab sisend parameetriks Kodutöö objekti.
- Muudab selle kodutöö omaduse tehtud väärtuse tõeseks.
- Eemaldab selle kodutöö tegemataKodutööd listist.
- Lisab selle kodutöö tehtudKodutööd listi.

### ÜL 2.7

Looge klassis Õpilane funktsioon tagastaTehtudKodutööd(self), mis teeb järgmist:
- Käib tsükliga läbi tehtudKodutööd listi ning prindib iga kodutöö pealkiri omaduse.

### ÜL 2.8

Looge klassis Õpilane funktsioon tagastaHindelisedKodutööd(self), mis teeb järgmist:
- Käib tsükliga läbi tegemataKodutööd listi ning kontrollib **kas** kodutöö on hindeline (mõelge millist Kodutöö omadust me peame kontrollima).
    - Kui kodutöö **on** hindeline, siis prinditakse kodutöö pealkiri.

## Kontrollimine
Looge klassi väliselt Õpilane objekt, näiteks järgmiste omadustega:
- nimi: "Joosep Joosepson"
- kursus: "ABC21"

Looge kaks Kodutöö objekti näiteks järgmiste omadustega:
- pealkiri: "Esse mingil teemal"
- hindeline: False


- pealkiri: "Kirjand mingil teemal"
- hindeline: True

Lisage lisaKodutöö funktsiooniga mõlemad kodutööd õpilasele. Käivitage tagastaTegemataKodutööd funktsioon ja see peaks tagastama:
- Tegemata on:  Esse mingil teemal
- Tegemata on:  Kirjand mingil teemal

Käivitage tagastaHindelisedKodutööd funktsioon ning see peaks tagastama:
- Hindeline kodutöö on:  Kirjand mingil teemal

Käivitage märgiKodutööTehtud funktsioon ning andke sisendiks esimene kodutöö. Peale seda käivitage tagastaTehtudKodutööd funktsioon ning tulemuseks peaks olema:
- Tehtud on:  Kirjand mingil teemal

