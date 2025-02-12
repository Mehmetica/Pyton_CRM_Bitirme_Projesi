from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt  # Alignment için doğru modül
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from admin_menu_preferences import AdminMenuPreferencesWindow
import sys
from user_menu import UserMenuWindow

class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setFixedSize(400, 300)  # Pencere boyutunu sabitler

        # Arka plan resmi ayari
        # Form.setStyleSheet(
        #     "background-image: url('/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/login.jpg'); background-repeat: no-repeat; background-position: center;"
        # )

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setPixmap(QtGui.QPixmap("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/diger_dosyalar/login.jpg"))

        # Başlik
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(50, 20, 300, 50)
        self.label_title.setText("CRM PROJECT")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")

        # Username etiketi
        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setGeometry(50, 100, 100, 30)
        self.label_username.setText("Username:")
        self.label_username.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")


        # Username giriş kutusu
        self.line_login_username = QtWidgets.QLineEdit(Form)
        self.line_login_username.setGeometry(150, 100, 200, 30)
        self.line_login_username.setStyleSheet(
            "background-color: #FFFFFF; border: 1px solid #000000; border-radius: 5px; color:black; "
        )

        # Password etiketi
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(50, 150, 100, 30)
        self.label_password.setText("Password:")
        self.label_password.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")

        # Password giriş kutusu
        self.line_login_password = QtWidgets.QLineEdit(Form)
        self.line_login_password.setGeometry(150, 150, 200, 30)
        self.line_login_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_login_password.setStyleSheet(
            "background-color: #FFFFFF; border: 1px solid #000000; border-radius: 5px; color:black;"
        )

        # Login butonu
        self.push_login_login = QtWidgets.QPushButton(Form)
        self.push_login_login.setGeometry(100, 220, 100, 30)
        self.push_login_login.setText("Login")
        self.push_login_login.setStyleSheet(
            "background-color: #FFC107; color: black; font-weight: bold; border-radius: 5px;"
        )

        # Exit butonu
        self.push_login_exit = QtWidgets.QPushButton(Form)
        self.push_login_exit.setGeometry(210, 220, 100, 30)
        self.push_login_exit.setText("Exit")
        self.push_login_exit.setStyleSheet(
            "background-color: #FFC107; color: black; font-weight: bold; border-radius: 5px;"
        )


# Google Sheets API bağlantisi
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/credentials.json", scopes=scope)#json dosyasi nerdeyse onun konumunu gir ki karisiklik olmasin
#  creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
client = gspread.authorize(creds)



def get_users_from_drive():
    """Google Drive'dan kullanicilari çeker ve DataFrame olarak döndürür."""
    try:
        # Yeni dosya adi veya ID ile bağlan
        sheet = client.open("Kullanicilar").sheet1  # Google Sheets adi client.open("Kullanicilar").sheet1.sheet.get_all_records()[2]
        data = sheet.get_all_records()
        ############################
        # print(data)
        return pd.DataFrame(data)
    except gspread.exceptions.SpreadsheetNotFound:
        raise FileNotFoundError("Google Sheets 'Kullanicilar' çalişma kitabi bulunamadi!")
    except Exception as e:
        raise Exception(f"Google Sheets'e bağlanirken bir hata oluştu: {str(e)}")
    
  


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.push_login_login.clicked.connect(self.validate_login)
        self.ui.push_login_exit.clicked.connect(self.close_application)
        self.users_df = get_users_from_drive()

    def validate_login(self):
        """Kullanici adi ve şifreyi Google Drive'daki verilerle doğrular."""
        username = self.ui.line_login_username.text()
        password = self.ui.line_login_password.text()

        # Kullanıcıyı filtrele
        user = self.users_df[
            (self.users_df['kullanici'] == username) & (self.users_df['parola'] == password)
        ]

        if not user.empty:  # Eğer kullanıcı bulunduysa
            yetki = user.iloc[0]['yetki']  # Kullanıcının yetkisini al
            if yetki == 'admin':
                self.open_admin_menu()
            elif yetki == 'user':
                self.open_user_menu()
            else:
                QtWidgets.QMessageBox.warning(self, "Login Failed", "Unknown role detected.")
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")


    def open_admin_menu(self):
        """Başarili giriş sonrasi Admin Menu ekranini açar."""
        self.admin_menu = AdminMenuPreferencesWindow()
        self.admin_menu.show()
        self.close()

    def open_user_menu(self):
        self.user_menu = UserMenuWindow()
        self.user_menu.show()
        self.close()


    def close_application(self):
        """Uygulamayi kapatir."""
        QtWidgets.QApplication.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
