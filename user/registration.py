from kivy.uix.screenmanager import Screen
import mysql.connector



class RegistrationScreen(Screen):
    def build(self):
        pass

    def regis_button_checker(self):
        dzwignia = True
        if self.ids.userpassword.text != self.ids.userpasswordagain.text:
            pass
        else:
            connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                                 host='127.0.0.1', database='yourworldonline',
                                                 auth_plugin='mysql_native_password')

            cursor = connection.cursor(buffered=True)
            email = self.ids.useremail.text
            emailn = (email,)
            queryusermail = "SELECT email FROM users WHERE email=%s"
            cursor.execute(queryusermail, emailn)
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
            queryusername = "SELECT username FROM users WHERE username=%s"
            cursor.execute(queryusername, usern)
            for nameUN in cursor:
                if self.ids.userlogin.text in nameUN:
                    dzwignia = False
                    pass
            if dzwignia is True:
                connection = mysql.connector.connect(user='root',
                                                     password='Wikingowie123x',
                                                     host='127.0.0.1', database='yourworldonline',
                                                     auth_plugin='mysql_native_password')

                cursor = connection.cursor(buffered=True)

                insertquery = "INSERT INTO users(username, userscol," \
                              " email, experience) VALUES(%(username)s, %(userscol)s, %(email)s, %(experience)s)"

                insertdata = {'username': self.ids.userlogin.text,
                              'userscol': self.ids.userpassword.text,
                              'email': self.ids.useremail.text,
                              'experience': 0}

                cursor.execute(insertquery, insertdata)
                connection.commit()
                connection.close()
                self.manager.current = "login"
                connection.close()