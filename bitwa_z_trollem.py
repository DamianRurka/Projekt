imie = input('Podaj Nickname:')
from time import sleep
import random
item4 = ['Sierp Żniwiarza']
trole = random.randint(2, 10)
hp = 200
obrazenia = 4
zabite_trole = 0
wytrzymalosc_broni = 50
wytrzymalosc_zbroi = 70
z = 'zloto'
k = 'kamien wskrzeszenia'
wybor = ""
bitwy = 0
podroze = 0
sila = 1  # dodaj zwiekszenie mocy poprzez poswiecenie 20pkt hp (albo skrzynia albo oltarz -poswiecenie krwii)
# Inwentarz bohatera
# Demonstruje tworzenie

ekwipunek = ()

if not ekwipunek:
    print("WITAJ W GRZE: \n\n\n\t\t\tMONSTER SLAYER ")
    print("\n\n\n\nNie masz nic \nAle posiadasz:", hp, "punktów życia")
    print("\nUwazaj na siebie", imie, " i dokonuj przemyślanych wyborów! \nRyzyko również moze sie oplacic!")
input("\nAby kontynuować misję, naciśnij klawisz Enter.")
print('w piwnicy znalazłeś skrzynię \nZabierasz znajdujace sie w niej przedmioty')
ekwipunek = ["miecz",
             "zbroja"]
# wyświetl każdy element 
for przedmioty in ekwipunek:
    print(przedmioty)
input("\n\nAby kontynuować  podróż, naciśnij klawisz enter ")
while bitwy != 20:
    import random

    trole = random.randint(2, 10)
    print('\n\n\n\n\n\n\nwyruszyłeś w podróż i napotkałeś bande', trole, ' trolli')
    if hp <= 0:
        print('Zostałeś pokonany')
        break
    while trole != 0 and bitwy != 20:
        trole -= sila
        zabite_trole += 1
        hp -= obrazenia
        wytrzymalosc_broni -= 1
        wytrzymalosc_zbroi -= 1
        if wytrzymalosc_zbroi == 0:
            obrazenia += 4
            del ekwipunek[1]
            sleep(3)
            print('\n\nTwoja zbroja ulegla zniszczeniu')
            print('Otrzymywane obrazenia wrastają 2-krotnie')
        if hp <= 0:
            print('Zostałeś pokonany')
            break
        elif trole <= 0:
            print('pokonales potwory i ')
            bitwy += 1
        if wytrzymalosc_broni <= 0:
            del ekwipunek[0]
            print('twój miecz pękł ')
            if not 'miecz' in ekwipunek:
                print(' \nZ racji że nie posiadałeś broni by się bronić \nZostałeś zjedzony')
                hp = 0
                break
    if hp <= 0:
        break
    print('pozostało ci: ', hp, 'punktów życia')
    print('\nUwazaj ! Wytrzymałosc twojej broni spada: ', wytrzymalosc_broni, '/ 50')
    item1 = ['zloto']
    item2 = ['mikstura']
    item3 = ['miecz']
    item4 = ['Sierp Żniwiarza']
    skrzynia = ["zloto-1", "mikstura-2", "oselka-3"]
    print('\nZnalazles skrzynię w ktorej znajdują się:\n', skrzynia, )

    print('\nwybierz ktory przedmiot zabierasz')
    wybor = input('podaj cyfrę przypisaną do przedmiotu: ')
    if wybor == '1':
        ekwipunek += item1
    elif wybor == '3':
        print('\n\n\n\n\nZebrałeś osełke ,Twa broń została naprawiona ')
        wytrzymalosc_broni = 50
    elif wybor == '2':
        hp += 50
        print('\n\n\n\n\t\tSpożyłeś miksturę \ntwoje punkty życia wzrosły i posiadasz ich teraz :', hp, )
    print('aktualna liczba posiadanych przedmiotów: ', len(ekwipunek))
    print('posiadane przedmioty:  ')
    for przedmioty in ekwipunek:
        print(przedmioty)
    print("\n\t\t\tstoczone bitwy :", bitwy)
    print("\n\t\t\tpokonane stwory:", zabite_trole)
    if bitwy == 10:
        sleep(3)
        print('\nDotarłeś do ołtarza : \nW zamian za twą krew twoja siła wzrośnie ')
        x = input('\nWpisz "krew" aby poświecić 50pkt swojego życia')
        if x == 'krew':
            hp -= 50
            trole -= 1
if bitwy == 20:
    print('W skrzyni znalazłeś: ', item4, ' \nPotęzny Artefakt ,kilkakrotnie Silniejszy \nniż twój pordzewiały miecz ')
    print("\n\nTwa Broń: SIERP ŻNIWIARZA \nAktywuje z czasem Tajemną Specjalną Umiejętność!")
    krwiopijca = random.randint(1, 10)

    ekwipunek += item4
    sleep(3)
    print('przebrnąłeś przez całą jaskinię')
    sleep(3)
    print('\n\n\t\t....')
    sleep(3)
    print('\n\n\t\t\tO NIE ! ')
    sleep(3)
    print('\t\t\t\nNiestety czeka cie ostateczna walka z : "GOBLIN LORD" ')
    HP = 1000
    GOBLIN_LORD_HP = ["GOBLIN LORD", HP]
    GOBLIN = (
        """
             |------------|
            \    O    O    /
             |      ×     |
              \ |------|  /
                \_______/    ||||
              ____|  |_____  / /
          / / |           | / /
        | |   |   o   o   |
        | |   |           |
        ||||  |_____*_____|
              |  |    |  |
              [][]    [][]
    """,
        """
             |------------|
            \    O    O    /
             |      ×     |
              \ |------|  /
                \_______/  
              ____|  |_____ 
          / / |           | 
        | |   |   o   o   |
        | |   |           |
        ||||  |_____*_____|
              |  |    |  |
              [][]    [][]
    """,
        """
             |------------|
            \    \    /    /
             |      ×     |
              \ |------|  /
                \_______/  
              ____|  |_____ 
              |           | 
              |   o   o   |
              |           |
              |_____*_____|
              |  |    |  |
              [][]    [][]
    """,
        """                   
          ____|  |____
          |          |
          |   o   o  |        /-----------/
          |          |       \  x     x    /
          |____*_____|        |     ×     |
           |  |  |  |         |   -----   |
           [][]  [][]          \_________/
                                  |  |
    """)
    while HP > 1 or hp > 1:
        lifestell = random.randint(5, 11)
        if HP >= 500:
            print('\n\t\t\t', HP)
            print(GOBLIN[0])
            input('atak \n"enter" ')
            hp -= 4
            HP -= 10
            print('Potwór cię uderzył \nPozostalo ci:', hp, 'hp')
            if hp <= 0:
                print('Zostales pokonany')
                break
        elif HP >= 300 and HP < 500:
            print('\n\t\t\t', HP)
            print("ODCIALES REKE GOBLINA \nTWA SZANSA NA ZWYCIESTWO ROSNIE!")
            print(GOBLIN[1])
            input('atak \n"enter" ')
            print('twa broń pochłania:', lifestell)
            hp = hp + lifestell
            HP -= 10
            hp -= 4
            print('Potwór cię uderzył Głową \nPozostalo ci:', hp, 'hp')
            if hp <= 0:
                print('Zostales pokonany')
                break
        elif HP >= 1 and HP < 300:
            print("ODCIALES DRUGA REKE GOBLINA \nTWA SZANSA NA ZWYCIESTWO ROSNIE????")
            print(' \nGOBLIN JEST WSCIEKLY!!!!')
            print('\n\n\n\n\t\t\t', HP)
            print(GOBLIN[2])
            input('atak \n"eneter" ')
            hp = hp + lifestell
            HP -= 15
            hp -= 18
            print('Potwór cię uderzył NOGA \nPozostalo ci:', hp, 'hp')
            if hp <= 0:
                print('Zostales Pokonany')
                break
        elif HP <= 0:
            print('\n\n\n\n\t\t\tHP=0')
            print('\n\t\t\tPOKONALES GOBLINA!!!')
            print(GOBLIN[3])
            input('\n\n\nAby zakonczyc wcisnij enter')
            break

