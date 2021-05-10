# Ülesanne 1
Ülesandeks on kirjeldada 2 klassi, Menüü ja Toit. Menüü klass sisaldab enda omadusena listi, kus hoiame erinevaid toite, mida menüü pakub.

### ÜL 1.1
Looge PyCharmis 2 faili:

- Toit.py
- Menüü.py

### ÜL 1.2
Toit.py failis kirjeldage klass Toit ja selle init meetod, millel on vähemalt järgmised omadused:
- **nimetus**, kus hoiame roa nimetust (tekst).
- **hind**, kus hoiame roa hinda (komakohaga arv)
- **päevaEri**, kus hoiame Boolean, ehk True või False väärtust (vaikimisi võiks see olla False). Kui väärtus on True, siis see toit on menüü eri pakkumine.

Nende omaduste väärtused peavad olema init meetodis antud **sisend parameetritena**. Nii same igat toitu kirjeldades anda erinevad väärtused.

### ÜL 1.3
Menüü.py failis kirjeldage klass Menüü ja selle init meetod, millel on vähemalt järgmised omadused:
- **pealkiri**, kus hoiame menüü või restorani pealkirja (tekst).
- **toidud**, list kus hoiame erinevad Road objektid. Alguses peab see list tühi olema.

### ÜL 1.4
Looge klassis Menüü funktsioon lisaToit(self), mis võtab sisend parameetriks ühe Toit objekti.

Funktsioon peab menüü "toidud" list-tüüpi omadusse lisama sisendina antud Toit objekti.

### ÜL 1.5
Looge klassis Menüü funktsioon kuvaToidudJaHinnad(self), mis prindib kõik omaduses "toidud" olevad Toit objektide nimetus ja hind omadused.

### ÜL 1.6
Looge klassis Menüü funktsioon kuvaPäevaEri(self), mis prindib omaduses "toidud" olevad Toit objektide nimetus ja hind omadused, ainult juhul kui Toit objekti on päeva eripakkumine.

### ÜL 1.7
Looge klassis Menüü funktsioon leiaKallimToit(self), mis prindib omaduses "toidud" oleva kõige kallima hinnaga Toit objekti nimetuse ja hinna.

### ÜL 1.8
Looge klassist väljas uus muutuja, kuhu loote Menüü objekti. Menüü objektile võite pealkirja omadusele väärtuse ise välja mõelda.

Looge klassist väljas 3 uut muutujat ning igasse muutujasse looge uus Toit objekt, näiteks järgmiste omadustega:

- nimetus: Ühepaja toit
- hind: 3.75


- nimetus: Sealiha guljašš
- hind: 4.25
  

- nimetus: Pasta bolognese
- hind: 3.00


Lisage need toidud Menüüle toitude listi.

Käivitage ülesannetes 1.4 kuni 1.7 loodud Menüü funktsioonid. Funktsioonid peaks tulemuseks tagastama näiteks:
- Ühepaja toit 3.75
- Sealiha guljašš 4.25
- Pasta bolognese 3.0


- Päeva eri: Pasta bolognese 3.0


- Kõige kallim toit: Sealiha guljašš 4.25