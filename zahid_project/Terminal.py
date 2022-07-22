import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import sqlite3


class WelComeScreen(QDialog):
    def __int__(self):
        super(WelComeScreen, self).__int__()
        loadUi("Welcomescreen.ui",self)
        self.login.click.connect(self.gotologin)

    def gotologin (self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(Widget.currentIndex()+1)

class loginScreen(QDialog):
    def __int__(self):
        super(loginScreen, self).__int__()
        loadUi("login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.password)
        self.login.clicked.connect(self.loginfuction)

    def loginfunction(self, result_pass=None):
        user=self.emailfield.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("please input all fields.")

        else:
            conn= sqlite3.connect("shop_data.db")
            cur= conn.cursor()
            query= 'SELECT password FROM login_info WHERE username =\''+user+"\'"
            cur.execute(query)
            result_pass== cur.fetchone()[0]
            if result_pass == password:
                print("Succrssfully loggein.")
            else:
                self.error.setText("Invalid username or password")
            



#main
app =QApplication(sys.argv)
welcome = WelComeScreen()
Widget = QtWidgets.QStackedWidget()
Widget.addWidget(welcome)
Widget.setFixedHeight(800)
Widget.setFixedWidth(1200)
Widget.show()
try:
    sys.exit(app.exec_())
except:
    print("exiting")
