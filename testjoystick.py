

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView
from kivy.app import App
from touch import MyMapView
import requests
import smtplib, ssl
import autopep8
import pycodestyle
import mysql.connector
import my_map_view


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

"""

#############################################################################################
                                          #GLOBALNE!!!!!!!
USER_ID=None
USER_NAME=None
PIONOWA_POZYCJA_GRACZA=40.41362602642995
POZIOMA_POZYCJA_GRACZA=-3.6819590868909984
DZWIGNIAPOBORU = True


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
        global USER_ID
        USER_ID = 1
        global USER_NAME
        USER_NAME = "Seph"
        global PIONOWA_POZYCJA_GRACZA
        PIONOWA_POZYCJA_GRACZA = "51.1276481"
        global POZIOMA_POZYCJA_GRACZA
        POZIOMA_POZYCJA_GRACZA = "16.9936345"

        self.manager.current = "UserPlatformFunctions"


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

    def buttonUP(self):
        self.LoadPlayerObject(0, 1)

    def button_RIGHT(self):
        self.LoadPlayerObject(1, 0)

    def button_LEFT(self):
        self.LoadPlayerObject(-1, 0)

    def button_DOWN(self):
        self.LoadPlayerObject(0, -1)

    def LoadPlayerObject(self, horizontalDirection=0, verticalDirection=0):
        horizontalSpeed = 0.0001
        verticalSpeed = 0.0002
        print(self.ids.mapview.lat, self.ids.mapview.lon)
        self.PLAYER_POSITION(
            self.ids.mapview.lon + horizontalSpeed * horizontalDirection,
            self.ids.mapview.lat + verticalSpeed * verticalDirection
        )

    def PLAYER_POSITION(self, lon, lat):
        playerpos = self.ids.PLAYER_POSITION
        playerpos.lat = lat
        playerpos.lon = lon
        mapposition = self.ids.mapview
        mapposition.center_on(lat, lon)


    def WORLD_MAP_ITEMS_LOAD(self):
        pass

    def LoadingPlayerPosFromDataBase(self):
        pass
        #wykonanie tej funkcji umieść na początku funkcji       LOAD PLAYER OBJECT
        #wczytaj dane o pozycji gracza

    #         connection = mysql.connector.connect(user='root', password='Wikingowie123x',
    #                                              host='127.0.0.1', database='yourworldonline',
    #                                              auth_plugin='mysql_native_password')
    #
    #         cursor = connection.cursor(buffered=True)
    #
    #         #ZAPIS DANYCH
    #
    #         insertQuery = "INSERT INTO users(username, userscol, email) VALUES(%(username)s, %(userscol)s, %(email)s)"
    #         insertData = {'username': '11111111', 'userscol': '111', 'email': '11111'}
    #
    #         cursor.execute(insertQuery, insertData)
    #
    #         connection.commit()

    def BuildingsOnMap(self):
        pass
        #Zbuduj funkcję randomowego respawnu budynków w losowych lokalizacjach lub wczytuj
        # lokalizacje tych budynków z bazy danych

        # MapMarkerPopup:
        # id: ikonaBUDYNKU
        # source: obraz budynku.PNG
        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        # lat: 40.41362602642995
        # lon: -3.6819590868909984
        # on_lat:
        # print(self.lat, self.lon)
        # on press: wyswietl mini okno sklepu

    def RespawnMonstersObjects(self):
        pass

    def LoadMonstersAndStatisticsFromDatabase(self):
        pass

    def GoToFightFightersScreenWhenObjectsCollideOrUserTouchObject(self):
        pass


####################################################################################################
# FIGHT SCREEN       PVE

#PO Wygranej Bitwie zapisz w bazie danych postęp gracza-zdobyte przedmioty i doświadczenie i
# wróć do okna eksploracji swiata

# class FightFigters():
#     pass

#    def BackToExploreWorldWhenFightEnd(self):
#        pass
#  oblugadanych():
#     def run(self):
#
#         connection = mysql.connector.connect(user='root', password='Wikingowie123x',
#                                              host='127.0.0.1', database='yourworldonline',
#                                              auth_plugin='mysql_native_password')
#
#         cursor = connection.cursor(buffered=True)
#
#         #ZAPIS DANYCH
#
#         insertQuery = "INSERT INTO users(username, userscol, email) VALUES(%(username)s, %(userscol)s, %(email)s)"
#         insertData = {'username': '11111111', 'userscol': '111', 'email': '11111'}
#
#         cursor.execute(insertQuery, insertData)
#
#         connection.commit()
#
#         #POBIERANIE DANYCH
#
#         query = 'SELECT id,username,userscol,email FROM users'          #pobieranie danych
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
# WIDGET SCREENS

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
#####################################################################################################
# LOAD PLAYERDATA AND REFRESH/UPLOAD ON DATABASE
# class
