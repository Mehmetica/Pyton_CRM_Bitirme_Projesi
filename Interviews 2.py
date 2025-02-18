


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView, QLineEdit, QVBoxLayout, QTableWidgetItem, QAbstractItemView, QWidget, QHBoxLayout
import sys
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import os


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 481)
        Form.setMinimumSize(QtCore.QSize(681, 481))
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, -10, 681, 491))
        self.label.setMinimumSize(QtCore.QSize(681, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 391, 51))
        self.label_2.setMinimumSize(QtCore.QSize(391, 51))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(223, 194, 107);  /* Arka plan rengi */\n"
"color: rgb(2, 50, 90);  /* Yazı rengi */\n"
"border-radius: 10px;  /* Köşeleri yuvarlat */\n"
"padding: 5px;  /* Buton içindeki boşluk */")
        self.label_2.setObjectName("label_2")
        self.lineEdit_search = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_search.setGeometry(QtCore.QRect(240, 80, 271, 21))
        self.lineEdit_search.setStyleSheet("  border-radius: 10px; /* Yuvarlak köşeler */")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_search = QtWidgets.QPushButton(parent=Form)
        self.pushButton_search.setGeometry(QtCore.QRect(100, 80, 121, 21))
        self.pushButton_search.setStyleSheet("QPushButton {\n"
"    background-color: rgb(2, 50, 90); /* Yeşil arka plan */\n"
"    color: white; /* Beyaz yazı */\n"
"    border-radius: 10px; /* Yuvarlak köşeler */\n"
"    border: 2px solid rgb(223, 194, 107); /* Siyah kenarlık */\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
"}\n"
"")
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_search.clicked.connect(self.search_user)
        self.pushButton__exit = QtWidgets.QPushButton(parent=Form)
        self.pushButton__exit.setGeometry(QtCore.QRect(590, 430, 75, 24))
        self.pushButton__exit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(209, 0, 0); /* Yeşil arka plan */\n"
"    color: white; /* Beyaz yazı */\n"
"    border-radius: 10px; /* Yuvarlak köşeler */\n"
"    border: 2px solid #000000; /* Siyah kenarlık */\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
"}")
        self.pushButton__exit.setObjectName("pushButton__exit")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(50, 140, 601, 271))
        self.frame.setMinimumSize(QtCore.QSize(601, 271))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #F0F0F0; /* Açık gri arka plan */\n"
"    border: 2px solid black; /* Siyah kenarlık */\n"
"    border-radius: 10px; /* Yuvarlatılmış köşeler */\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 20, 521, 221))
        self.tableWidget_2.setMinimumSize(QtCore.QSize(521, 221))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(521, 221))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(240, 240, 240);\n"
"    gridline-color: #D5D8DC; /* Grid çizgileri için açık gri */\n"
"    border: 1px solid #BDC3C7; /* Çerçeve rengi */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(2, 50, 90); /* Başlıkların arka planı */\n"
"    color: white; /* Beyaz yazı */\n"
"    font: bold 12px \"Tahoma\";\n"
"    border: 1px solid #2980B9;\n"
"}\n"
"")
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.pushButton_submitted = QtWidgets.QPushButton(parent=Form)
        self.pushButton_submitted.setGeometry(QtCore.QRect(110, 120, 131, 31))
        self.pushButton_submitted.setStyleSheet("QPushButton {\n"
"    background-color: rgb(2, 50, 90); /* Yeşil arka plan */\n"
"    color: white; /* Beyaz yazı */\n"
"    border-radius: 10px; /* Yuvarlak köşeler */\n"
"    border: 2px solid #000000; /* Siyah kenarlık */\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
"}")
        self.pushButton_submitted.setObjectName("pushButton_submitted")
        self.pushButton_submitted.clicked.connect(self.show_submitted_projects)
        self.pushButton_Received = QtWidgets.QPushButton(parent=Form)
        self.pushButton_Received.setGeometry(QtCore.QRect(280, 120, 131, 31))
        self.pushButton_Received.setStyleSheet("QPushButton {\n"
"    background-color: rgb(2, 50, 90); /* Yeşil arka plan */\n"
"    color: white; /* Beyaz yazı */\n"
"    border-radius: 10px; /* Yuvarlak köşeler */\n"
"    border: 2px solid #000000; /* Siyah kenarlık */\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
"}")
        self.pushButton_Received.setObjectName("pushButton_Received")
        self.pushButton_Received.clicked.connect(self.show_received_projects)
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 120, 131, 31))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(2, 50, 90); /* Yeşil arka plan */\n"
"    color: white; /* Beyaz yazı */\n"
"    border-radius: 10px; /* Yuvarlak köşeler */\n"
"    border: 2px solid #000000; /* Siyah kenarlık */\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_main_menu)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "                      CRM- Interviews"))
        self.lineEdit_search.setPlaceholderText(_translate("Form", "Enter text to search..."))
        self.pushButton_search.setText(_translate("Form", "Search"))
        self.pushButton__exit.setText(_translate("Form", "Exit"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Fullname"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Project Submission Date"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Project Development Date"))
        self.pushButton_submitted.setText(_translate("Form", "Projects Submitted"))
        self.pushButton_Received.setText(_translate("Form", "Projects Received"))
        self.pushButton_4.setText(_translate("Form", "Main Menu"))

    def search_user(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials_path = os.path.join(os.getcwd(), "credentials.json")
        creds = Credentials.from_service_account_file(credentials_path, scopes=scope)
        client = gspread.authorize(creds)
        print("Google Sheets'e bağlanıldı.")

           # Dosya ID'si (File ID)
        file_id = "1JdqyvaA-sdjcxHPTeaVml0KPke5RX_5s7SSf29BuF9U"  # Buraya kendi File ID'nizi yazın

            # Dosyayı aç
        sheet = client.open_by_key("1JdqyvaA-sdjcxHPTeaVml0KPke5RX_5s7SSf29BuF9U").sheet1  # Dosyanın ilk sayfasını seç
        print("Dosya başarıyla açıldı.")
        records = sheet.get_all_records()
        print(f"Toplam kayıt sayısı: {len(records)}")

        df = pd.DataFrame(records)
        headers = list(records[0].keys()) if records else []
        self.tableWidget_2.setColumnCount(len(headers))  # Sütun sayısını ayarla
        self.tableWidget_2.setHorizontalHeaderLabels(headers)  # Başlıkları ayarla

            # LineEdit'ten alınan arama terimi
        search_text = self.lineEdit_search.text().strip()
    
        if search_text:
            # Belirtilen sütunda arama yap (Örneğin "Ad" sütunu)
            filtered_df = df[df['Adınız Soyadınız'].astype(str).str.contains(search_text, case=False, na=False)]
            print(filtered_df)


                 
             # Tabloyu güvenli şekilde temizle
            while self.tableWidget_2.rowCount() > 0:
                    self.tableWidget_2.removeRow(0)

            for row_idx, row in enumerate(filtered_df.itertuples(index=False)):
                self.tableWidget_2.insertRow(row_idx)
                for col_idx, value in enumerate(row):  
                    self.tableWidget_2.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def show_submitted_projects(self):
         scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
         credentials_path = os.path.join(os.getcwd(), "credentials.json")
         creds = Credentials.from_service_account_file(credentials_path, scopes=scope)
         client = gspread.authorize(creds)

         # Google Sheets dosyasını aç
         file_id = "1JdqyvaA-sdjcxHPTeaVml0KPke5RX_5s7SSf29BuF9U"  # Kendi dosya ID'nizi ekleyin
         sheet = client.open_by_key(file_id).sheet1

         # Google Sheets'ten verileri al
         records = sheet.get_all_records()
         df = pd.DataFrame(records)

         # Eğer "İsim" veya "Proje Gönderiliş Tarihi" sütunu yoksa hata vermesin
         if "Adınız Soyadınız" not in df.columns or "Proje gonderilis tarihi" not in df.columns:
                 print("Hata: 'İsim' veya 'Proje Gönderiliş Tarihi' sütunu bulunamadı!")
                 return

         # "Proje Gönderiliş Tarihi" sütunu boş olmayanları filtrele
         filtered_df = df[df["Proje gonderilis tarihi"].notna()][["Adınız Soyadınız", "Proje gonderilis tarihi"]]

         # Eğer hiç veri yoksa kullanıcıya bildir
         if filtered_df.empty:
                 print("Proje gönderiliş tarihi bulunan kayıt yok.")
                 return

         # PyQt TableWidget'ı temizle ve başlıkları güncelle
         self.tableWidget_2.clearContents()
         self.tableWidget_2.setRowCount(0)
         self.tableWidget_2.setColumnCount(2)  # Sadece 2 sütun gösterilecek
         self.tableWidget_2.setHorizontalHeaderLabels(["İsim", "Proje Gönderiliş Tarihi"])
      
         # Verileri tabloya ekle
         for row_idx, row in enumerate(filtered_df.itertuples(index=False)):
                 self.tableWidget_2.insertRow(row_idx)
                 self.tableWidget_2.setItem(row_idx, 0, QTableWidgetItem(str(row[0])))  # İsim
                 self.tableWidget_2.setItem(row_idx, 1, QTableWidgetItem(str(row[1])))  # Proje Gönderiliş Tarihi

                 print(f"{len(filtered_df)} kişi listelendi.")

    def show_received_projects(self):
         scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
         credentials_path = os.path.join(os.getcwd(), "credentials.json")
         creds = Credentials.from_service_account_file(credentials_path, scopes=scope)
         client = gspread.authorize(creds)

        
         file_id = "1JdqyvaA-sdjcxHPTeaVml0KPke5RX_5s7SSf29BuF9U"  # Kendi dosya ID'nizi ekleyin
         sheet = client.open_by_key(file_id).sheet1

         
         records = sheet.get_all_records()
         df = pd.DataFrame(records)

         
         if "Adınız Soyadınız" not in df.columns or "Projenin gelis tarihi" not in df.columns:
                 print("Hata: 'İsim' veya 'Proje Gelis Tarihi' sütunu bulunamadı!")
                 return

         
         filtered_df = df[df["Projenin gelis tarihi"].notna()][["Adınız Soyadınız", "Projenin gelis tarihi"]]

         
         if filtered_df.empty:
                 print("Proje geliş tarihi bulunan kayıt yok.")
                 return

         
         self.tableWidget_2.clearContents()
         self.tableWidget_2.setRowCount(0)
         self.tableWidget_2.setColumnCount(2)  # Sadece 2 sütun gösterilecek
         self.tableWidget_2.setHorizontalHeaderLabels(["İsim", "Proje Gelis Tarihi"])
      
         # Verileri tabloya ekle
         for row_idx, row in enumerate(filtered_df.itertuples(index=False)):
                 self.tableWidget_2.insertRow(row_idx)
                 self.tableWidget_2.setItem(row_idx, 0, QTableWidgetItem(str(row[0])))  # İsim
                 self.tableWidget_2.setItem(row_idx, 1, QTableWidgetItem(str(row[1])))  # Proje Gönderiliş Tarihi

                 print(f"{len(filtered_df)} kişi listelendi.")

    def show_main_menu(self):
        # Main Menu butonu işlevi
         if self.previous_window:
            self.previous_window.show()
         else:
            from user_menu import UserMenuWindow
            user_menu= UserMenuWindow()
            user_menu.show()
         self.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
