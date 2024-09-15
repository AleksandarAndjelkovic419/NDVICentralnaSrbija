**prikaz srednje temperature vazduha, vlaznosti vazduha i padavina za Beograd za period jul 2021.godine.**
Ovaj projekat prvo ucitava *praznu listu* u kojoj ce se cuvati podaci.
Zatim se otvara i cita .csv fajl koji sadrzi podatke potrebne za pravljenje grafikona(*podaci koji su uzeti su radjeni za mapu*).
Konvertujemo listu u Numpy niz.
Vadimo podatke iz fajla koji su nam potrebni za projekat (*datum,temperaturu,vlaznost, vazduha i kolicinu padavina*).
Pretvaramo datume u stringove.
Pravimo grafikon za temperaturu (u Celizijusima) pri cemu se koristi funkcija [plt].
Isto se radi i za vlaznost vaduha i kolicinu padavina.
Na kraju se pravi statistika, gde se radi srednja mesecna temperatura vazduha za ceo mesec(funkcijom [mean]).
Isto se radi i za Vlaznost vazduha, dok se za kolicinu padavina radi kumulativno sabiranje za ceo mesec, posto se kolicina padavina ne deli broj dana u mesecu (funcija [sum]).
