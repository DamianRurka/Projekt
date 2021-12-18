class PARAMETRYBOHATER:
    def __init__(self, nazwa_bohatera,poziom,statystyki,inwentarz,wyposazenie):
        self.nazwa_bohatera = nazwa_bohatera
        self.poziom = poziom
        self.statystyki = statystyki           #<zaladuj tu funkcje/klase statystyki self.STATYSTYKI()
        self.inwentarz = inwentarz
        self.wyposazenie = wyposazenie
        self.separator = ('_' * 50)

    def __str__(self):
        return f"bohater: {self.nazwa_bohatera},\nPoziom bohatera: {self.poziom}"

    def __repr__(self):

        return f"\nbohater: {self.nazwa_bohatera}\nPoziom bohatera: {self.poziom}\n"

    def __int__(self):
        return self.poziom

    def __bool__(self):
        return self.poziom >=20

    def __getitem__(self, item):
        return self.inwentarz.get(item , 'Brak przedmiotu')

    def __setitem__(self, item, value):
        print(f'dodawanie: {value} sztuk {item} do inwentarza')
        if item in self.inwentarz.keys():
         self.inwentarz[item] += value
        else:
            self.inwentarz[item] = value

    def __iter__(self):
        for k, v in self.inwentarz.items():
            yield self
    #def __next__(self):




bohater1 = PARAMETRYBOHATER("Prince_Of_Hell" , 1 , {'ATAK' : 10,'HP' : 100 },
                           {'mikstura_hp':10,'mikstura_ataku':1},
                           {"bron" : "miecz"})

bohater2 = PARAMETRYBOHATER("ZEUS" , 2 , {'ATAK' : 11,'HP' : 110 },
                           {'mikstura_hp':10,'mikstura_ataku':1},
                           {"bron" : "miecz"})

bohater3 = PARAMETRYBOHATER("Venom" , 3 , {'ATAK' : 12,'HP' : 120 },
                           {'mikstura_hp':10,'mikstura_ataku':1},
                           {"bron" : "miecz"})

heroes = [bohater1,bohater2,bohater3]

#print(bohater2)  #def__str__(self) wypisuje jedną zmienną i jej parametry
# print(heroes)     #def __repr__(self)  wypisuje LISTE bohaterów w zmiennej heroes
# print(int(bohater2))       #def__int__(self) zwraca tylko liczby!!!!
# print(bool(bohater3))      #Zwraca true i false ( mozna uzyc do sprawdzenia czy
                           # bohater ma odpowiedni poziom by nosić wyposażenie które wymaga odpowiedniego poziomu

# print(str(bohater2))
# print(bohater2.__str__())

print('mikstura uzdrowienia: ',bohater2['mikstura_hp']) #getitem printowanie zawartości slownika bohater2
print('lopata:',bohater2['lopata'])      #jesli nie ma podanego klucza printuje : Brak przedmiotu

bohater2['lopata'] = 1
print(f"lopata:{bohater2['lopata']}")    #setitem dodawanie do inwentarza jeśli go nie ma : Else

bohater2['mikstura_hp'] = 200      #setitem dodawanie dropu z moba do przedmiotów które juz są,: If
print(f"mikstura uzdrowienia:{bohater2['mikstura_hp']}")

for element,liczba in bohater2:
    print(f"Bohater {bohater2.nazwa_bohatera} ma {liczba} sztuk {element} ")

for element,liczba in bohater2:
    print(f"{liczba} {element}")        #def iter ,-1