from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView
from kivy.app import App

screen_helper = """
<UsersPlayGameOnMap>:
    MapView:
        size_hint: 1, 1
        id: mapview
        lat: 40.41362602642995
        lon: -3.6819590868909984 
        zoom:19        
        max_zoom : 19
        min_zoom :19
        MapMarkerPopup:
            id: PLAYER_POSITION
            source: "img/Knight/Attack/5.png"
            lat: 40.41362602642995
            lon: -3.6819590868909984    
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


class UsersPlayGameOnMap(FloatLayout):

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
        print(App.get_running_app().root.ids.mapview.lat, App.get_running_app().root.ids.mapview.lon)
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


class MyApp(MDApp):
    def build(self):
        return UsersPlayGameOnMap()


Builder.load_string(screen_helper)
MyApp().run()