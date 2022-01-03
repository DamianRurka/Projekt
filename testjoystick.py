from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy.app import App
from my_map_view import MyMapView
from kivy.core.audio import SoundLoader
import requests
import smtplib, ssl
import autopep8
import pycodestyle
import mysql.connector
import my_map_view
import random
from time import sleep

#########################################################################################
# Okna Aplikacji
screen_helper = """
ScreenManager:
    MenuScreen:
    LoginScreen:
    RegistrationScreen:
    EmailScreen:
    UsersPlatform:
    UsersPlayGameOnMap:
    FightFighters:

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
    MyMapView:
        id: mapview
        double_tap_zoom: False
        lat: 40.41362602642995
        lon: -3.6819590868909984
         
        zoom:19        
        max_zoom : 19
        min_zoom :19
        MapMarkerPopup:
            id: PLAYER_POSITION
            lat: 40.41362602642995
            lon: -3.6819590868909984 
            source: "img/Knight/Attack/5.png"
        MapMarker:
            id: Monsters_position
            lat:
            lon:
            Button:
                on_release:
                             
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
        on_press: root.button_RIGHT()
    MDIconButton :
        id : idz_w_lewo   
        icon : "arrow-left-bold-box-outline"       
        pos_hint : {'center_x':0.35,'center_y':0.1}
        user_font_size : 40 
        on_press: root.button_LEFT()
    MDRoundFlatButton: 
        text: "SAVE LOCATION"
        font_size: 12
        pos_hint: {"center_x":0.5,"center_y":0.98}
        on_press: root.Save_Location_IN_DataBASE()
    MDRoundFlatButton: 
        text: "BACK TO YOUR SAVE LOCATION"
        font_size: 12
        pos_hint: {"center_x":0.5,"center_y":0.89}
        on_press: root.PLAYER_POSITION_FROMDATABASE()

<FightFighters>:
    name: 'Battle'
    id : battlessc
    FitImage: 
        source: "img/Background/background.png"
        id : battlescreen
    MDIconButton :
        id : player   
        icon : 'img/Knight/Attack/5.png'     
        pos_hint : {'center_x':0.1,'center_y':0.4}
        user_font_size : 80
        
    MDIconButton :
        id : monster  
        icon : 'img/goblin.png'       
        pos_hint : {'center_x':0.9,'center_y':0.4}
        user_font_size : 80 
        on_press: root.petla_walki()

"""

#############################################################################################
# GLOBALNE!!!!!!!
USER_ID = None
USER_NAME = None
PIONOWA_POZYCJA_GRACZA = None
POZIOMA_POZYCJA_GRACZA = None
DZWIGNIAPOBORU = True
licznik = 0
PLAYEREXPERIENCE = 0
PLAYER_LV = 1

#############################################################################################
# WELCOME SCREEN

class MenuScreen(Screen):
    pass


###############################################################################################
# LOGIN FUNCTION
class LoginScreen(Screen):

    def build(self):
        pass

    def check_player_lv(self):
        if PLAYEREXPERIENCE >= 0 and PLAYEREXPERIENCE <= 299:
            self.LV = 1
        elif PLAYEREXPERIENCE > 300 and PLAYEREXPERIENCE <= 999:
            self.LV = 2
        elif PLAYEREXPERIENCE > 1000 and PLAYEREXPERIENCE <= 2000:
            self.LV = 3
        elif PLAYEREXPERIENCE > 2001 and PLAYEREXPERIENCE <= 4500:
            self.LV = 4
        elif PLAYEREXPERIENCE > 4501 and PLAYEREXPERIENCE <= 10000:
            self.LV = 5
        elif PLAYEREXPERIENCE > 10001 and PLAYEREXPERIENCE <= 17000:
            self.LV = 6
        elif PLAYEREXPERIENCE > 17001 and PLAYEREXPERIENCE <= 29000:
            self.LV = 7
        elif PLAYEREXPERIENCE > 29001 and PLAYEREXPERIENCE <= 45000:
            self.LV = 8
        elif PLAYEREXPERIENCE > 45001 and PLAYEREXPERIENCE <= 67000:
            self.LV = 9
        elif PLAYEREXPERIENCE > 67001:
            self.LV = 10
        global PLAYER_LV
        PLAYER_LV = self.LV

    def login_button_checker(self):

        connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                             host='127.0.0.1', database='yourworldonline',
                                             auth_plugin='mysql_native_password')

        cursorPS = connection.cursor(buffered=True)
        username = self.ids.userlogin.text
        usercheck = (username,)
        datacheck = "SELECT id,username,userscol,pozycjapionowa,pozycjapozioma,experience FROM users WHERE username=%s"
        cursorPS.execute(datacheck, usercheck)

        for row in cursorPS:
            if self.ids.userlogin.text and self.ids.userpassword.text in row:
                global USER_ID
                USER_ID = row[0]
                global USER_NAME
                USER_NAME = row[1]
                global PIONOWA_POZYCJA_GRACZA
                PIONOWA_POZYCJA_GRACZA = row[3]
                global POZIOMA_POZYCJA_GRACZA
                POZIOMA_POZYCJA_GRACZA = row[4]
                intexp = int(row[5])
                global PLAYEREXPERIENCE
                PLAYEREXPERIENCE = int(intexp)

                self.manager.current = "UserPlatformFunctions"
                self.check_player_lv()

        connection.close()


########################################################################################
# REGISTRATION FUNCTION

class RegistrationScreen(Screen):
    def build(self):
        pass

    def regis_button_checker(self):
        dzwignia = True
        self.haslo1 = self.ids.userpassword.text
        self.haslo2 = self.ids.userpasswordagain.text
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
                              " email, experience) VALUES(%(username)s, %(userscol)s, %(email)s, %(experience)s)"

                insertData = {'username': self.ids.userlogin.text,
                              'userscol': self.ids.userpassword.text,
                              'email': self.ids.useremail.text,
                              'experience': 0}

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
# FUNKCJA OBSLUGUJACA EKWIPUNEK,INWENTARZ, LECZENIE BOHATERA,
# STATYSTYKI I UMIEJETNOSCI I ZAPISUJACA/AKTUALIZUJACA JE W BAZIE DANYCH

class UsersPlatform(Screen):
    def build(self):
        pass


####################################################################################################
# Przeniesienie do okna i klasy Bitwa w przypadku zderzenia obiektów (gracz-mob)
# +wprowadzenie do funkcji BuildYourWorld(Parcels,buildings town
# Stworzenie funkcji generujacej stwory wokół gracza jesli mniej niz 5 generuj dodatkową randomową ilość od 2 do 5


class UsersPlayGameOnMap(Screen):

    def Save_Location_IN_DataBASE(self):
        global PIONOWA_POZYCJA_GRACZA
        PIONOWA_POZYCJA_GRACZA = self.ids.PLAYER_POSITION.lon
        global POZIOMA_POZYCJA_GRACZA
        POZIOMA_POZYCJA_GRACZA = self.ids.PLAYER_POSITION.lat
        self.PLAYER_POSITION_FROMDATABASE()

        connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                                     host='127.0.0.1', database='yourworldonline',
                                                     auth_plugin='mysql_native_password')

        cursor = connection.cursor(buffered=True)
        pozycjapionowa= self.ids.PLAYER_POSITION.lon
        pozycjapozioma= self.ids.PLAYER_POSITION.lat
        username = USER_NAME
        usernlondi = (pozycjapionowa,username,)
        usernlandi= (pozycjapozioma,username,)
        Querylonditude = "UPDATE users set pozycjapionowa = %s WHERE username=%s"
        cursor.execute(Querylonditude, usernlondi)
        Querylanditude = "UPDATE users set pozycjapozioma = %sWHERE username=%s"
        cursor.execute(Querylanditude, usernlandi)


        connection.commit()
        if connection.is_connected():
            cursor.close()
            connection.close()


    def PLAYER_POSITION_FROMDATABASE(self):
        playerpos = self.ids.PLAYER_POSITION
        playerpos.lat = PIONOWA_POZYCJA_GRACZA
        playerpos.lon = POZIOMA_POZYCJA_GRACZA
        mapposition = self.ids.mapview
        mapposition.center_on(playerpos.lat, playerpos.lon)


    def MonsterLocationsGenerator(self):
        global licznik
        licznik += 1
        if licznik == 5:
            lokalizacjalat = self.ids.PLAYER_POSITION.lat
            zakresdolny = lokalizacjalat + 0.001
            zakresgorny = lokalizacjalat - 0.001
            randomlatitude = random.uniform(zakresgorny, zakresdolny)

            lokalizacjalon = self.ids.PLAYER_POSITION.lon
            zakresprawo = lokalizacjalon - 0.001
            zakreslewo = lokalizacjalon + 0.001
            randomlonditude = random.uniform(zakresprawo, zakreslewo)
            randommonster = random.randint(1, 2)

            if randommonster == 1:
                imgmonster = "img/myicons/goblin.jfif"
            else:
                imgmonster= "img/myicons/dragon.jfif"
            self.m1 = MapMarkerPopup(lon=randomlonditude, lat=randomlatitude,
                                source=imgmonster)
            self.m1.placeholder = Button(text="Fight with\n monster!", x=70, y=400, on_release=self.GoToFightScreen )
            self.ids.mapview.add_marker(self.m1)
            licznik = 0

    def buttonUP(self):
        self.LoadPlayerObject(0, 1)
        self.MonsterLocationsGenerator()

    def button_RIGHT(self):
        self.LoadPlayerObject(1, 0)
        self.MonsterLocationsGenerator()

    def button_LEFT(self):
        self.LoadPlayerObject(-1, 0)
        self.MonsterLocationsGenerator()

    def button_DOWN(self):
        self.LoadPlayerObject(0, -1)
        self.MonsterLocationsGenerator()

    def LoadPlayerObject(self, horizontalDirection=0, verticalDirection=0):
        horizontalSpeed = 0.0001
        verticalSpeed = 0.0002
        self.PLAYER_POSITION(
            self.ids.mapview.lon + horizontalSpeed * horizontalDirection,
            self.ids.mapview.lat + verticalSpeed * verticalDirection
        )

    def PLAYER_POSITION(self, lon, lat):
        self.playerpos = self.ids.PLAYER_POSITION
        self.playerpos.lat = lat
        self.playerpos.lon = lon
        mapposition = self.ids.mapview
        mapposition.center_on(lat, lon)

    def BuildingsOnMap(self):
        pass
        # Zbuduj funkcję budowania budynków w lokalizacjach wybranych przez gracza i
        # zapisuj lokalizacje budynków w bazie danych i

    def LoadBuildingsFromDataBase(self):
        pass

    def GoToFightScreen(self, dummy):
        self.manager.current = "Battle"
        self.ids.mapview.remove_marker(self.m1)
        pass

####################################################################################################
# FIGHT SCREEN   PVE
# PO Wygranej Bitwie zapisz w bazie danych postęp gracza-zdobyte przedmioty i doświadczenie i
# wróć do okna eksploracji swiata


class FightFighters(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_hp = 200
        self.monsterHP = 100

    def petla_walki(self):
        self.monsterstrenght = random.randint(2, 20)
        self.player_strenght = (8 * PLAYER_LV * 0.75) + random.randint(2, 10)
        self.monsterHP -= self.player_strenght
        #zaatakowałeś stwora
        self.max_hp -= self.monsterstrenght
        #zostałeś zaatakowany
        print(self.monsterHP)
        print(self.max_hp)
        if self.monsterHP < 0:
            print('wygrana')
            global PLAYEREXPERIENCE
            PLAYEREXPERIENCE += random.randint(25, 100)
            self.monsterHP = 100
            self.max_hp = 200
            self.manager.current = 'screenmapmove'
            connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                                 host='127.0.0.1', database='yourworldonline',
                                                 auth_plugin='mysql_native_password')

            cursor = connection.cursor(buffered=True)
            username = USER_NAME
            userexp = (PLAYEREXPERIENCE, username,)
            Queryexp = "UPDATE users set experience = %s WHERE username=%s"
            cursor.execute(Queryexp, userexp)
            connection.commit()
            if connection.is_connected():
                cursor.close()
                connection.close()
            #wyswietl napis wygrana i po 1s cofnij uzytkownika do widoku

        elif self.max_hp < 0:
            self.monsterHP = 100
            self.max_hp = 200
            self.manager.current = 'screenmapmove'
            # przegrana,cofnij do widoku mapy
        # lblplayerhp = Label(text = str(self.max_hp))
        # lblmonsterhp = Label(text=str(self.monsterHP))
        #
        # FloatLayout.add_widget(lbl,)
        # return lbl

####################################################################################################
# WIDGET SCREENS

sm = ScreenManager()
sm.add_widget(UsersPlayGameOnMap(name='screenmapmove'))
sm.add_widget(FightFighters(name='Battle'))
sm.add_widget(UsersPlatform(name='UserPlatformFunctions'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegistrationScreen(name='Registration'))
sm.add_widget(EmailScreen(name='emailreminder'))

class YourWorldOnline(MDApp):

    def build(self):
        self.screen = Builder.load_string(screen_helper)
        self.sound = SoundLoader.load('img/myicons/music.mp3')
        self.sound.play()
        return self.screen

YourWorldOnline().run()
