"""
YourWorld ,MMO RPG, Mobilna gra turowa we wstępnej wersji 2D
na androida wykorzystująca:
kivy ,kivyMD, buildozzer , api googlemaps ,lokalizacje użytkownika
Gra oferuje użytkownikom rozwój postaci oraz "

dodatek do gry: posiadanie włości(prywatny obszar mapy) ,
 świat gry będzie rozdzielony na parcele/sektory
gracz na początku gry nie będzie posiadał żadnych włości , można je nabyć za odpowiednią kwotę waluty premium,
 lub oglądając reklamy ograniczona ilosc dziennie , po obejzeniu reklam użytkownik otrzymuje premium walute
 za którą może nabyć włości , posiadanie włości odblokowuje nowe funkcje gry:
  (mini gry/hazard, możliwośc budowy uzytecznych budunków-wymagane materialy do budowy ,włości wraz
  z budynkami mogą być odsprzedawane innym graczom by oni mogli przejąć bonusy płynące z:
   powstałej wioski/miasteczka. parcele/sektory można łaczyć / premium walute mozna przekazywac innym graczom
   stwórz system który blokuje tą mozliwość dla graczy ponizej 100lv tak by gracze nie tworzyli nub kont do zbierania
   premium waluty , badz stwórz rejest graczy którzy tylko ogladaja reklamy dla premium waluty ,
   po analizie danego konta perm ban . maksymalna ilość posiadanych parceli to łączny obszar około 2km kwadratowych
   uzytkownicy przebywający na czyimś obszarze płacą podatek dla wlasiciela parcelu w wysokości
   :gracz sam ustala podatek od możliwości korzystania z jego budynków . (przykładowo gracz wykupił
   2km kwadratowe parceli w gdańsku koło PKP , wybudował mnóstwo budynków które dostarczają specjalne
    skórki,zwierzaki,bonusy do rozwoju spelli ,jakieś mini gry itp , ustalił cenę korzystania z jego miasteczka na
    10PW  ZA MIESIAC -premium waluta .

ZABLOKUJ MOZLIWOS WEJSCIA POSTACI DO WODY BADZ JESLI TO NIEMOZLIWE , DORZUC FUNKCJE KTÓRA ZABIERA 25%HP CO 2SEKUNDY
, W PRZYPADKU ŚMIERCI COFNIJ BOHATERA DO MIEJSCA W KTÓRYM ZNAJDOWAŁ SIĘ 2MIN WCZEŚNIEJ , STWÓRZ FUNKCJE
PRZECHOWUJĄCĄ DANE O LOKALIZACJI AWATARA ZAPISUJ TO W BAZIE DANYCH MYSQL




"""


from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.mapview import MapView
import requests
import smtplib, ssl
import autopep8
import mysql.connector

#########################################################################################
                          #Okna Aplikacji
screen_helper = """
ScreenManager:
    MenuScreen:
    LoginScreen:
    RegistrationScreen:
    EmailScreen:
    UsersPlatform:
    UsersPlayGameOnMap:


<MenuScreen>:
    name: 'menu'
    FitImage:
        source: "img/ekran_logowania.png"
    MDRectangleFlatButton:
        text: 'Zaloguj'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'login'
    MDRectangleFlatButton:
        text: 'Zarejestruj'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'Registration'
    MDRectangleFlatButton:
        text: 'Zapomniałeś hasła ?'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'emailreminder'


<LoginScreen>:
    name: 'login'
    FitImage:
        source: "img/loginimmage.png"
    MDTextFieldRound:
        id: userlogin
        hint_text: "nazwa uzytkownika"
        icon_right: "account"
        size_hint_x: None
        width: 200
        font_size: 18
        pos_hint: {"center_x":0.5, "center_y":0.6}
    
    MDTextFieldRound:
        id: userpassword
        hint_text: "hasło"
        icon_right: "eye-off"
        icon_left: 'key-variant'
        size_hint_x: None
        width: 200
        font_size: 18
        pos_hint: {"center_x":0.5,"center_y":0.5}   
        password: True 
        
    MDRoundFlatButton: 
        text: "Zaloguj"
        font_size: 12
        pos_hint: {"center_x":0.5,"center_y":0.4}
        on_press: root.login_button_checker()   
    MDRectangleFlatButton:
        text: 'Powrót'
        pos_hint: {"center_x":0.5,"center_y":0.1}
        on_press: root.manager.current = 'menu'


<RegistrationScreen>:
    name: 'Registration'
    FitImage:
        source: "img/rejgisImage.png"
    MDTextFieldRound:
        id: userlogin
        hint_text: "nazwa użytkownika"
        min_text_length: 5
        icon_right: "account"
        size_hint_x: None
        width: 200
        font_size: 18
        pos_hint: {"center_x":0.5, "center_y":0.6}
    
    MDTextFieldRound:
        id: userpassword
        hint_text: "hasło"
        icon_right: "eye-off"
        icon_left: 'key-variant'
        max_text_length: 10
        min_text_length: 5
        size_hint_x: None
        width: 200
        font_size: 18
        pos_hint: {"center_x":0.5,"center_y":0.5}   
        password: True 
    
    MDTextFieldRound:
        id: userpasswordagain
        hint_text: "powtórz hasło"
        icon_right: "eye-off"
        size_hint_x: None
        width: 200
        font_size: 18
        pos_hint: {"center_x":0.5,"center_y":0.4}   
        password: True    
    
    MDTextFieldRound:
        id: useremail
        hint_text: "email"
        icon_right: "email"
        min_text_length: 9
        size_hint_x: None
        width: 200
        font_size: 18
        pos_hint: {"center_x":0.5,"center_y":0.3}   
    
    MDRoundFlatButton: 
        text: "Zarejestruj"
        font_size: 12
        pos_hint: {"center_x":0.5,"center_y":0.2}
        on_press: root.regis_button_checker()    
           
    MDRectangleFlatButton:
        text: 'Powrót'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'


<EmailScreen>:
    name: 'emailreminder'
    FitImage:
        source: "img/ekran.png"
    MDTextFieldRound:
        id: userlogin
        hint_text: "nazwa uzytkownika"
        icon_right: "account"
        size_hint_x: None
        width: 200
        font_size: 18
        pos_hint: {"center_x":0.5, "center_y":0.6}
    
    MDTextFieldRound:
        id: emailprzypomijhaslo
        hint_text: "email"
        icon_right: "email"
        size_hint_x: None
        width: 200
        font_size: 18
        pos_hint: {"center_x":0.5, "center_y":0.5}
    
    MDRoundFlatButton: 
        text: "Wyslij Haslo"
        font_size: 12
        pos_hint: {"center_x":0.5,"center_y":0.4}
        on_press: root.email_password_sender()

    MDRectangleFlatButton:
        text: 'Powrót'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'


<UsersPlatform>:
    name: 'UserPlatformFunctions'
    FitImage:
        source: "img/MenuUserPlatformheroitems.png"
    
    MDIconButton :   
        icon : "img/myicons/armors.png"       
        pos_hint : {'center_x':.06,'center_y':.86}
        user_font_size : 20   
    MDIconButton :   
        icon : "img/myicons/swords.png"       
        pos_hint : {'center_x':.06,'center_y':.96}
        user_font_size : 20
    MDIconButton :   
        icon : "img/myicons/potions.png"       
        pos_hint : {'center_x':.06,'center_y':.76}
        user_font_size : 20    
    MDIconButton :   
        icon : "treasure-chest"       
        pos_hint : {'center_x':.06,'center_y':.66}
        user_font_size : 40 
    MDIconButton :   
        icon : "crown"       
        pos_hint : {'center_x':.9,'center_y':.96}
        user_font_size : 40 
    
    MDRoundFlatIconButton:
        text: 'EXPLORE WORLD'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'screenmapmove'
        icon: "play"
        width: dp(250)
             

<UsersPlayGameOnMap>:
    name: 'screenmapmove'
    MapView:
        id: playerghost
        lat:10
        lon:10
        zoom:20
        on_lat:
            print('lat', self.lat)
        on_lon:
            print('lon', self.lon)

    Image:
        id: ikonabohatera
        source: "img/myicons/heromenuicon.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
    MDIconButton :
        icon : "apps-box" 
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : 40 
        on_press: root.manager.current = 'UserPlatformFunctions'
    MDIconButton : 
        id : idz_do_gory  
        icon : "arrow-up-bold-box-outline"       
        pos_hint : {'center_x':0.5,'center_y':0.18}
        user_font_size : 40 
        on_press: root.buttonUP()
    MDIconButton : 
        id : idz_do_dolu  
        icon : "arrow-down-bold-box-outline"       
        pos_hint : {'center_x':0.5,'center_y':0.1}
        user_font_size : 40 
        on_press: root.button_DOWN()
    MDIconButton : 
        id : idz_w_prawo  
        icon : "arrow-right-bold-box-outline"       
        pos_hint : {'center_x':0.65,'center_y':.1}
        user_font_size : 40 
        on_press: root.button_w_PRAWO()
    MDIconButton :
        id : idz_w_lewo   
        icon : "arrow-left-bold-box-outline"       
        pos_hint : {'center_x':0.35,'center_y':0.1}
        user_font_size : 40 
        on_press: root.button_w_LEWO()
            

"""
#############################################################################################
                                           # WELCOME SCREEN

class MenuScreen(Screen):
    pass

###############################################################################################

                                           # LOGIN FUNCTION
class LoginScreen(Screen):

    def build(self):
        pass

    def login_button_checker(self):

        connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                             host='127.0.0.1', database='yourworldonline',
                                             auth_plugin='mysql_native_password')

        cursorPS = connection.cursor(buffered=True)
        username = self.ids.userlogin.text
        usercheck = (username,)
        datacheck = "SELECT username,userscol FROM users WHERE username=%s"
        cursorPS.execute(datacheck, usercheck)

        for row in cursorPS:
            if self.ids.userlogin.text and self.ids.userpassword.text in row:
                self.manager.current = "UserPlatformFunctions"

        connection.close()

########################################################################################
                                         #REGISTRATION FUNCTION

class RegistrationScreen(Screen):
    def build(self):
        pass

    def regis_button_checker(self):
        dzwignia = True
        self.haslo1 = self.ids.userpassword.text
        self.haslo2= self.ids.userpasswordagain.text
        if self.haslo1 != self.haslo2:
            pass
        else:
            connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                                      host='127.0.0.1', database='yourworldonline',
                                                      auth_plugin='mysql_native_password')

            cursor = connection.cursor(buffered=True)
            email = self.ids.useremail.text
            emailn = (email,)
            Queryusermail = "SELECT email FROM users WHERE email=%s"
            cursor.execute(Queryusermail, emailn)
            for row_em in cursor:
                if self.ids.useremail.text in row_em:
                    dzwignia = False
                    pass

            connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                                 host='127.0.0.1', database='yourworldonline',
                                                 auth_plugin='mysql_native_password')

            cursor = connection.cursor(buffered=True)
            username = self.ids.userlogin.text
            usern = (username,)
            Queryusername = "SELECT username FROM users WHERE username=%s"
            cursor.execute(Queryusername, usern)
            for nameUN in cursor:
                if self.ids.userlogin.text in nameUN:
                    dzwignia = False
                    pass

            if dzwignia == True:
                connection = mysql.connector.connect(user='root',
                                                  password='Wikingowie123x',
                                                 host='127.0.0.1', database='yourworldonline',
                                                 auth_plugin='mysql_native_password')

                cursor = connection.cursor(buffered=True)

                insertQuery = "INSERT INTO users(username, userscol," \
                              " email) VALUES(%(username)s, %(userscol)s, %(email)s)"

                insertData = {'username': self.ids.userlogin.text,
                            'userscol': self.ids.userpassword.text,
                             'email': self.ids.useremail.text}

                cursor.execute(insertQuery, insertData)
                connection.commit()
                connection.close()
                self.manager.current = "login"
                connection.close()

#################################################################################################
                                     # SEND USER-PASSWORD TO EMAIL

class EmailScreen(Screen):
    pass

    def email_password_sender(self):

        connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                             host='127.0.0.1', database='yourworldonline',
                                             auth_plugin='mysql_native_password')

        cursor = connection.cursor(buffered=True)
        query = 'SELECT id,username,userscol,email FROM users'
        cursor.execute(query)

        for row in cursor:
            if self.ids.userlogin.text and self.ids.emailprzypomijhaslo.text in row:
                self.manager.current = "login"

                cursorPS = connection.cursor(buffered=True)
                email = self.ids.emailprzypomijhaslo.text
                my_data = (email,)
                Querypassword = "SELECT userscol FROM users WHERE email=%s"
                cursorPS.execute(Querypassword, my_data)

                for PS in cursorPS:
                    passw = str(PS)
                    port = 465
                    smtp_serwer = "smtp.gmail.com"
                    nadawca = "yourworldonlinemmo@gmail.com"
                    odbiorca = self.ids.emailprzypomijhaslo.text
                    syspush = "ofezwwmgprnbryof"
                    wiadomosc = """\
                            From: <yourworldonlinemmo@gmail.com>
                            To: 
                            Subject: Account

                            Witaj , oto twoje haslo:       
                            """ + passw

                    ssl_pol = ssl.create_default_context()

                    with smtplib.SMTP_SSL(smtp_serwer, port, context=ssl_pol) as serwer:
                        serwer.login(nadawca, syspush)
                        serwer.sendmail(nadawca, odbiorca, wiadomosc)

####################################################################################################
                                     # USERS GAME PLATFORM , MENU SCREEEN
#FUNKCJA OBSLUGUJACA EKWIPUNEK,INWENTARZ, LECZENIE BOHATERA,STATYSTYKI I UMIEJETNOSCI

class UsersPlatform(Screen):
    def build(self):
        pass

####################################################################################################
                                    #PLAYGAME ArrowKeys , GOOGLEMAPS ,
                         #Przeniesienie do okna i klasy Bitwa w przypadku zderzenia obiektów (gracz-mob)
                     # +wprowadzenie do funkcji BuildYourWorld(Parcels,buildings town
        # Stworzenie funkcji generujacej stwory wokół gracza jesli mniej niz 5 generuj dodatkową randomową ilość od 2 do 5


class UsersPlayGameOnMap(Screen):


    def buttonUP(self):
        self.pressUP = True

        self.pressDOWN = False
        self.pressLEFT = False
        self.pressRIGHT = False

        self.LoadPlayerObject()
        return self.ids.idz_do_gory


    def button_w_PRAWO(self):
        self.pressRIGHT = True

        self.pressDOWN = False
        self.pressUP = False
        self.pressLEFT = False

        self.LoadPlayerObject()
        return self.ids.idz_w_prawo


    def button_w_LEWO(self):
        self.pressLEFT = True

        self.pressRIGHT = False
        self.pressDOWN = False
        self.pressUP = False

        self.LoadPlayerObject()
        return self.ids.idz_w_lewo


    def button_DOWN(self):
        self.pressDOWN = True

        self.pressUP = False
        self.pressLEFT = False
        self.pressRIGHT = False

        self.LoadPlayerObject()
        return self.ids.idz_do_dolu

    def LoadPlayerObject(self):


        player = self.ids.ikonabohatera.pos_hint
        currentx = player['center_x']
        currenty = player['center_y']
        if self.pressUP == True:
            currenty +=0.025

        if self.pressDOWN == True:
            currenty -=0.025

        if self.pressLEFT == True:
            currentx -=0.025

        if self.pressRIGHT == True:
            currentx +=0.025

        player = {'center_x': currentx,'center_y': currenty}

        self.ids.ikonabohatera.pos_hint = player

    def WORLD_MAP_LOAD(self):
        marker = MapMarkerPopup(lat=10,lon=12)
        self.root.add_widget(marker)

    def RespawnMonstersObjects(self):
        pass

    def LoadMonstersAndStatisticsFromDatabase(self):
        pass

    def GoToFightFightersScreenWhenObjectsCollide(self):
        pass


####################################################################################################
                                          #FIGHT SCREEN       PVE
#class FightFigters():
#     pass

#    def BackToExploreWorldWhenFightEnd(self):
#        pass

#####################################################################################################
                        #LOAD PLAYERDATA AND REFRESH/UPLOAD ON DATABASE
# class oblugadanych():
#     def run(self):
#
#         connection = mysql.connector.connect(user='root', password='Wikingowie123x',
#                                              host='127.0.0.1', database='yourworldonline',
#                                              auth_plugin='mysql_native_password')
#
#         cursor = connection.cursor(buffered=True)
#
#         insertQuery = "INSERT INTO users(username, userscol, email) VALUES(%(username)s, %(userscol)s, %(email)s)"
#         insertData = {'username': '11111111', 'userscol': '111', 'email': '11111'}
#
#         cursor.execute(insertQuery, insertData)
#
#         connection.commit()
#
#         query = 'SELECT id,username,userscol,email FROM users'
#         cursor.execute(query)
#
#         for row in cursor:
#             if "damian" in row:
#                 print(True)
#
#
#         connection.close()  # przerwanie połączenia
#
#
# oblugadanych().run()
####################################################################################################
                                       #WIDGET SCREENS

sm = ScreenManager()
sm.add_widget(UsersPlayGameOnMap(name='screenmapmove'))
sm.add_widget(UsersPlatform(name='UserPlatformFunctions'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegistrationScreen(name='Registration'))
sm.add_widget(EmailScreen(name='emailreminder'))

class YourWorldOnline(MDApp):

    def build(self):
        self.screen = Builder.load_string(screen_helper)
        return self.screen

YourWorldOnline().run()
