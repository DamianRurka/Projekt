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
            id: player_position
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
        on_press: root.button_up()
    MDIconButton : 
        id : idz_do_dolu  
        icon : "arrow-down-bold-box-outline"       
        pos_hint : {'center_x':0.5,'center_y':0.1}
        user_font_size : 40 
        on_press: root.button_down()

    MDIconButton : 
        id : idz_w_prawo  
        icon : "arrow-right-bold-box-outline"       
        pos_hint : {'center_x':0.65,'center_y':.1}
        user_font_size : 40 
        on_press: root.button_right()
    MDIconButton :
        id : idz_w_lewo   
        icon : "arrow-left-bold-box-outline"       
        pos_hint : {'center_x':0.35,'center_y':0.1}
        user_font_size : 40 
        on_press: root.button_left()
    MDRoundFlatButton: 
        text: "SAVE LOCATION"
        font_size: 12
        pos_hint: {"center_x":0.5,"center_y":0.98}
        on_press: root.save_location_in_database()
    MDRoundFlatButton: 
        text: "BACK TO YOUR SAVE LOCATION"
        font_size: 12
        pos_hint: {"center_x":0.5,"center_y":0.89}
        on_press: root.player_position_from_database()

<FightFighters>:
    name: 'Battle'
    id : battlessc
    FitImage: 
        source: 'img/myicons/bagna.png'
        id : battlescreen
    MDIconButton :
        id : player   
        icon : 'img/Knight/Attack/5.png'     
        pos_hint : {'center_x':0.1,'center_y':0.4}
        user_font_size : 80
    Label:
        text:''
        id:nick
        pos_hint : {'center_x':0.1,'center_y':0.6}
    Label:
        text:''
        id:playerhp
        pos_hint : {'center_x':0.1,'center_y':0.7}
    Label:
        text:''
        id:enemyhp
        pos_hint : {'center_x':0.9,'center_y':0.7}
    Label:
        text:''
        id: monstername
        pos_hint : {'center_x':0.9,'center_y':0.6}

    MDIconButton :
        id : monster  
        icon : 'img/myicons/goblin.png'       
        pos_hint : {'center_x':0.9,'center_y':0.4}
        user_font_size : 80 
        on_press: root.petla_walki()

"""