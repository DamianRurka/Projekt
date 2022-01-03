# Projekt Gry z przeznaczeniem na urządzenia mobilne.
gra YourWorldOnline 
W grze użytkownik ma możliwość nieskończonego eksplorowania świata opartego o openstreetmaps za pomocą strzałek jak i wstępnego rozwoju bohatera.

Aplikację uruchamia się w Pycharm za pomocą kombinacji klawiszy : Shift + F10 bądź strzałki Run . Aplikacji nie da się uruchomić z terminala,
do poprawnego działania aplikacji niezbędne jest zainstalowanie bibliotek znajdujących się w pliku requirements.txt jak i stworzenie bazy danych w MySQL Workbench:



user='root', password='Wikingowie123x',host='127.0.0.1', database='yourworldonline',

Aplikacja obsługuje tylko jedną tabelę i kolumny do niej przypisane:
tabela: users
kolumny:id , username , email , userscol , pozycjapionowa , pozycjapozioma , experience



Aby zacząć korzystanie z aplikacji użytkownik musi zarejestrować konto ,gdy rejestracja przebiegnie pomyślnie , użytkownik zostanie automatycznie przeniesiony do okna logowania .

W przypadku utraty dostępu do konta użytkownik może odzyskać dostęp poprzez funkcję programu "Zapomniałeś hasła?"
Gdy Użytkownik wpisze poprawną nazwę użytkownika oraz email ekran zostanie przęłączony na ekran logowania 
a na podaną skrzynkę mailową zostanie wysłana wiadomość z hasłem użytkownika .

Gdy Logowanie Przebiegnie pomyślnie ekran zostanie przełączony na okno menu gry .
Grę rozpocząć  można klikając w orzycisk Explore World

Za pomocą klawiszy na ekranie gry można poruszać postacią , gdy bohater się porusza , na ekranie pojawiają się przeciwnicy w losowych lokalizacjach.
Aby rozpocząć walkę z przeciwnikiem , trzeba kliknąć na niego po czym wyświetli się przycisk "Fight With Monster" , kliknięcie tego przycisku przeniesie użytkownika do 
okna bitwy . 

Walka odbywa się turowo w kolejności pierwszy: gracz ,drugi : przeciwnik
aby zaatakować przeciwnika wystarczy kliknąć na niego.

W Przypadku przegranej jak i wygranej potyczki , gracz zostanie automatycznie przeniesiony do okna widoku mapy,
lecz tylko w przypadku wygranej gracz otrzyma losową liczbę doświadczenia dzięki której można zwiększyć moc bohatera

Gracz zawsze rozpoczyna rozgrywkę w centrum stolicy hiszpanii ,
lecz eksplorując grę może zapisać swoją lokalizację klikając 2-krotnie przycisk 'Save Location' znajdujący się u góry ekranu.

Powracając do gry użytkownik może powrócić do zapisanej lokalizacji klikając w przycisk 'Back To Your Save Location" znajdujący się również u góry ekranu .

