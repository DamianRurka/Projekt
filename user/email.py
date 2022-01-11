from kivy.uix.screenmanager import Screen
import smtplib
import ssl
import mysql.connector


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

                cursorps = connection.cursor(buffered=True)
                email = self.ids.emailprzypomijhaslo.text
                my_data = (email,)
                querypassword = "SELECT userscol FROM users WHERE email=%s"
                cursorps.execute(querypassword, my_data)

                for ps in cursorps:
                    passw = str(ps)
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
