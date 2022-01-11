from kivy.uix.button import Button
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapMarkerPopup
from kivy.core.audio import SoundLoader
import mysql.connector
import random
from screen_helper import screen_helper
from user.registration import RegistrationScreen
from user.email import EmailScreen
from user.usermenu import UsersPlatform
import my_map_view

USER_ID = None
USER_NAME = None
PIONOWA_POZYCJA_GRACZA = None
POZIOMA_POZYCJA_GRACZA = None
LICZNIK = 0
PLAYEREXPERIENCE = 0
PLAYER_LV = 1
BACKGROUND = ''
MONSTER_ICON = ''


class MenuScreen(Screen):
    pass


class LoginScreen(Screen):
    def build(self):
        pass

    def check_player_lv(self):
        self.level = 1
        if PLAYEREXPERIENCE > 300:
            self.level = 2
        if PLAYEREXPERIENCE > 1000:
            self.level = 3
        if PLAYEREXPERIENCE > 2001:
            self.level = 4
        if PLAYEREXPERIENCE > 4501:
            self.level = 5
        if PLAYEREXPERIENCE > 10001:
            self.level = 6
        if PLAYEREXPERIENCE > 17001:
            self.level = 7
        if PLAYEREXPERIENCE > 29001:
            self.level = 8
        if PLAYEREXPERIENCE > 45001:
            self.level = 9
        if PLAYEREXPERIENCE > 67001:
            self.level = 10

        global PLAYER_LV
        PLAYER_LV = self.level

    def login_button_checker(self):
        connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                             host='127.0.0.1', database='yourworldonline',
                                             auth_plugin='mysql_native_password')

        cursorps = connection.cursor(buffered=True)
        username = self.ids.userlogin.text
        usercheck = (username,)
        datacheck = "SELECT id,username,userscol,pozycjapionowa,pozycjapozioma,experience FROM users WHERE username=%s"
        cursorps.execute(datacheck, usercheck)

        for row in cursorps:
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
                PLAYEREXPERIENCE = intexp
                self.manager.current = "UserPlatformFunctions"
                self.check_player_lv()
        connection.close()


class UsersPlayGameOnMap(Screen):
    def save_location_in_database(self):
        global PIONOWA_POZYCJA_GRACZA
        PIONOWA_POZYCJA_GRACZA = self.ids.player_position.lon
        global POZIOMA_POZYCJA_GRACZA
        POZIOMA_POZYCJA_GRACZA = self.ids.player_position.lat
        self.player_position_from_database()
        connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                             host='127.0.0.1', database='yourworldonline',
                                             auth_plugin='mysql_native_password')

        cursor = connection.cursor(buffered=True)
        pozycjapionowa = self.ids.player_position.lon
        pozycjapozioma = self.ids.player_position.lat
        username = USER_NAME
        usernlondi = (pozycjapionowa, username,)
        usernlandi = (pozycjapozioma, username,)
        querylonditude = "UPDATE users set pozycjapionowa = %s WHERE username=%s"
        cursor.execute(querylonditude, usernlondi)
        querylanditude = "UPDATE users set pozycjapozioma = %sWHERE username=%s"
        cursor.execute(querylanditude, usernlandi)
        connection.commit()
        if connection.is_connected():
            cursor.close()
            connection.close()

    def player_position_from_database(self):
        playerpos = self.ids.player_position
        playerpos.lat = PIONOWA_POZYCJA_GRACZA
        playerpos.lon = POZIOMA_POZYCJA_GRACZA
        mapposition = self.ids.mapview
        mapposition.center_on(playerpos.lat, playerpos.lon)

    def monster_locations_generator(self):
        global LICZNIK
        LICZNIK += 1
        if LICZNIK == 5:
            lokalizacjalat = self.ids.player_position.lat
            zakresdolny = lokalizacjalat + 0.001
            zakresgorny = lokalizacjalat - 0.001
            randomlatitude = random.uniform(zakresgorny, zakresdolny)
            lokalizacjalon = self.ids.player_position.lon
            zakresprawo = lokalizacjalon - 0.001
            zakreslewo = lokalizacjalon + 0.001
            randomlonditude = random.uniform(zakresprawo, zakreslewo)
            randommonster = random.randint(1, 2)
            if randommonster == 1:
                imgmonster = "img/myicons/goblin.png"
                self.m1 = MapMarkerPopup(lon=randomlonditude, lat=randomlatitude,
                                         source=imgmonster)

                self.m1.placeholder = Button(text="Fight with\n monster!",
                                             x=70, y=400, on_release=self.go_to_fight_goblin)
                self.ids.mapview.add_marker(self.m1)
            elif randommonster == 2:
                imgmonster = "img/myicons/dragon.png"
                self.m2 = MapMarkerPopup(lon=randomlonditude, lat=randomlatitude,
                                         source=imgmonster)

                self.m2.placeholder = Button(text="Fight with\n monster!",
                                             x=70, y=400, on_release=self.go_to_fight_dragon)
                self.ids.mapview.add_marker(self.m2)
            LICZNIK = 0

    def button_up(self):
        self.load_player_object(0, 1)
        self.monster_locations_generator()

    def button_right(self):
        self.load_player_object(1, 0)
        self.monster_locations_generator()

    def button_left(self):
        self.load_player_object(-1, 0)
        self.monster_locations_generator()

    def button_down(self):
        self.load_player_object(0, -1)
        self.monster_locations_generator()

    def load_player_object(self, horizontal_direction=0, vertical_direction=0):
        horizontal_speed = 0.0001
        vertical_speed = 0.0002
        self.player_position(
            self.ids.mapview.lon + horizontal_speed * horizontal_direction,
            self.ids.mapview.lat + vertical_speed * vertical_direction
        )

    def player_position(self, lon, lat):
        self.playerpos = self.ids.player_position
        self.playerpos.lat = lat
        self.playerpos.lon = lon
        mapposition = self.ids.mapview
        mapposition.center_on(lat, lon)

    def go_to_fight_goblin(self, dummy):
        global BACKGROUND
        BACKGROUND = 'img/myicons/bagna.png'
        global MONSTER_ICON
        MONSTER_ICON = 'img/myicons/goblin.png'
        self.manager.current = "Battle"
        self.ids.mapview.remove_marker(self.m1)
        pass

    def go_to_fight_dragon(self, dummy):
        global BACKGROUND
        BACKGROUND = "img/Background/background.png"
        global MONSTER_ICON
        MONSTER_ICON = "img/myicons/dragon.png"
        self.manager.current = "Battle"
        self.ids.mapview.remove_marker(self.m2)
        pass


class FightFighters(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_hp = 200
        self.monsterHP = 100
        self.monsterstrenght = random.randint(2, 20)
        self.player_strenght = (8 * PLAYER_LV * 0.75) + random.randint(2, 10)

    def petla_walki(self):
        self.ids.monster.icon = MONSTER_ICON
        self.ids.battlescreen.source = BACKGROUND
        self.ids.nick.text = USER_NAME
        self.ids.monstername.text = 'Your Nemezis'
        self.monsterHP -= self.player_strenght
        self.max_hp -= self.monsterstrenght
        self.ids.playerhp.text = str(self.max_hp)
        self.ids.enemyhp.text = str(self.monsterHP)
        if self.monsterHP < 0:
            self.ids.playerhp.text = ''
            self.ids.enemyhp.text = ''
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
            queryexp = "UPDATE users set experience = %s WHERE username=%s"
            cursor.execute(queryexp, userexp)
            connection.commit()
            if connection.is_connected():
                cursor.close()
                connection.close()
        elif self.max_hp < 0:
            self.monsterHP = 100
            self.max_hp = 200
            self.manager.current = 'screenmapmove'


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
