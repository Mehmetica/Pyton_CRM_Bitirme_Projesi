from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView, QLineEdit, QVBoxLayout, QTableWidgetItem, QAbstractItemView, QWidget, QHBoxLayout
import sys
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
# from user_menu import UserMenuWindow

class MentorMeetingsWindow(QtWidgets.QWidget):

    def __init__(self, previous_window=None):
        super().__init__()
        self.previous_window = previous_window  # Önceki pencereyi sakla
        self.initUi()
        
        self.connect_to_drive()
        # self.check_google_sheets_headers() #drivedaki dosyanin basliklarini kontrol etmek icin kullandik

    def connect_to_drive(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/credentials.json", scopes=scope)#json dosyasi nerdeyse onun konumunu gir ki karisiklik olmasin
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open("Mentor").sheet1  # Assuming data is in the first sheet 
    
    # def check_google_sheets_headers(self):
    #     headers = self.sheet.row_values(1)  # İlk satırdaki başlıkları al
    #     print("Google Sheets'teki Sütun Başlıkları:", headers)  # Terminale yazdır

    def filter_table(self, column):#filtreli sutunlar olusturmak icin kullanilir
        search_text = self.filter_widgets[column].text().strip().lower()  # Arama metnini al

        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, column)  # Belirtilen sütundaki veriyi al
            if item:
                cell_text = item.text().strip().lower()
                self.tableWidget.setRowHidden(row, search_text not in cell_text)  # Eşleşmeyen satırları gizle


    def search_combo(self):#combo menuden secilen veriye gore filtrelemek icin kullanilir
        selected_option = self.combo_mentor_dropmenu.currentText().strip()  # ComboBox'ta seçilen değeri al
        all_records = self.sheet.get_all_records()  # Tüm verileri çek

        column_name = "Aday Durum"
        # "Aday Durum" sütununda eşleşen kayıtları filtrele
        results = [
            (
                r.get('Meeting Date', ''),
                r.get('Name Surname', ''),
                r.get('Mentor', ''),
                str(r.get('IT Knowledge', '')),
                str(r.get('Intensity', '')),
                r.get('Comments', '')
            )
            for r in all_records if r.get(column_name, '').strip().lower() == selected_option.lower()
        ]

        self.tableWidget.setRowCount(len(results))  # Tablodaki satır sayısını ayarla

        if not results:  # Eğer sonuç yoksa bir mesaj göster
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("No matches found."))
            return

        for row_idx, (meeting_date, name_surname, mentor, it_knowledge, intensity, comments) in enumerate(results):
            self.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(meeting_date))
            self.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(name_surname))
            self.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(mentor))
            self.tableWidget.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(it_knowledge))
            self.tableWidget.setItem(row_idx, 4, QtWidgets.QTableWidgetItem(intensity))
            self.tableWidget.setItem(row_idx, 5, QtWidgets.QTableWidgetItem(comments))


    def clear_table(self):#tabloyu ve lineeditleri temizlemek icin kullanilir
        self.tableWidget.setRowCount(0)  # Tüm satırları sil
        
        # Arama kutularını temizle
        self.line_mentor_search.clear()  # Name Surname arama kutusu
        for filter_widget in self.filter_widgets:  # Her sütundaki arama kutusunu temizle
            filter_widget.clear()
        
        # ComboBox'ı sıfırla (ilk seçeneğe geri döndür)
        self.combo_mentor_dropmenu.setCurrentIndex(0)

    
    def initUi(self):
    # Arama kutusuna "Enter" basılınca aramayı başlat
        self.line_mentor_search.returnPressed.connect(self.search_name)



    def search_name(self):
        search_text = self.line_mentor_search.text().strip().lower()  # Kullanıcının girdiği arama metni

        all_values = self.sheet.get_all_values()  # Tüm tabloyu çek (ama sadece Name Surname'e bakacağız)

        if not all_values:
            print("Google Sheets'ten veri alınamadı!")
            return

        headers = all_values[0]  # İlk satır başlıklar
        data_rows = all_values[1:]  # Başlıklar hariç tüm satırlar

        try:
            name_surname_index = headers.index("Name Surname")  # "Name Surname" sütununun indeksini al
        except ValueError:
            print("Error: 'Name Surname' sütunu bulunamadı!")
            return

        results = []
        for row in data_rows:
            if len(row) > name_surname_index:  # Eğer satır eksik değilse
                name_surname = row[name_surname_index].strip().lower()
                if search_text in name_surname:  # Arama metni varsa
                    results.append(row)  # Tüm satırı ekle

        self.tableWidget.setRowCount(len(results))  # Tablodaki satır sayısını ayarla

        if not results:  # Eğer sonuç yoksa bir mesaj göster
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("No matches found."))
            return

        for row_idx, row in enumerate(results):
            for col_idx, cell in enumerate(row):  # Bütün sütunları ekle
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(cell))

    def show_comment_details(self, row, column):#comment sutunu uzun oldugu icin okunmasi icin, uzerine tiklayinca calisan fonksiyon
        if column == 5:  # 5. sütun "Comments" sütunu
            comment_text = self.tableWidget.item(row, column).text()
            QtWidgets.QMessageBox.information(self, "Full Comment", comment_text)


    def show_all_meetings(self):
        expected_headers = ["Meeting Date", "Name Surname", "Mentor", "IT Knowledge", "Intensity", "Comments"]
        all_records = self.sheet.get_all_records(expected_headers=expected_headers)  # Verileri çek

        self.tableWidget.setRowCount(len(all_records))  # Satır sayısını ayarla

        for row_idx, record in enumerate(all_records):
            meeting_date = record.get("Meeting Date", "")
            name_surname = record.get("Name Surname", "")
            mentor = record.get("Mentor", "")
            it_knowledge = str(record.get("IT Knowledge", ""))
            intensity = str(record.get("Intensity", ""))
            comments = record.get("Comments", "")

            for col_idx, value in enumerate([meeting_date, name_surname, mentor, it_knowledge, intensity, comments]):
                item = QtWidgets.QTableWidgetItem(value)
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable)  # Kullanıcı değiştiremesin
                self.tableWidget.setItem(row_idx, col_idx, item)

    # def show_all_meetings(self):
    #     expected_headers = ["Meeting Date", "Name Surname", "Mentor", "IT Knowledge", "Intensity", "Comments"]
    #     all_records = self.sheet.get_all_records(expected_headers=expected_headers)  # Verileri çek, sozluk olarak bize dondurur

    #     # print("Çekilen Veriler:", all_records)  # Terminale yazdırarak kontrol et

    #     self.tableWidget.setRowCount(len(all_records))  # Satır sayısını ayarla

    #     for row_idx, record in enumerate(all_records):
    #         meeting_date = record.get("Meeting Date", "")
    #         name_surname = record.get("Name Surname", "")
    #         mentor = record.get("Mentor", "")
    #         it_knowledge =str(record.get("IT Knowledge", ""))
    #         intensity = str(record.get("Intensity", ""))
    #         comments = record.get("Comments", "")

    #         # print(f"{row_idx}: {meeting_date}, {name_surname}, {mentor}, {it_knowledge}, {intensity}, {comments}")  # Her satırı yazdır

    #         self.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(meeting_date))
    #         self.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(name_surname))
    #         self.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(mentor))
    #         self.tableWidget.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(it_knowledge))
    #         self.tableWidget.setItem(row_idx, 4, QtWidgets.QTableWidgetItem(intensity))
    #         self.tableWidget.setItem(row_idx, 5, QtWidgets.QTableWidgetItem(comments))


    def initUi(self):
        self.setObjectName("Form")
        self.resize(700, 464)
        self.setFixedSize(700, 464)

        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(0, -5, 700, 471))
        self.label.setPixmap(QtGui.QPixmap("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/background.jpg"))
        self.label.setScaledContents(True)

        self.label_mentor_header = QtWidgets.QLabel(parent=self)
        self.label_mentor_header.setGeometry(QtCore.QRect(120, 40, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(28)
        self.label_mentor_header.setFont(font)
        self.label_mentor_header.setStyleSheet("background-color: rgb(223, 194, 107); color: rgb(2, 50, 90); border-radius: 10px; padding: 5px;")
        self.label_mentor_header.setText("              Mentor Meeting")

        self.line_mentor_search = QtWidgets.QLineEdit(parent=self)
        self.line_mentor_search.setGeometry(QtCore.QRect(60, 110, 151, 21))
        self.line_mentor_search.setStyleSheet("border-radius: 10px;")
        
        
        self.push_mentor_search = QtWidgets.QPushButton("Search", parent=self)
        self.push_mentor_search.setGeometry(QtCore.QRect(220, 110, 81, 21))
        self.push_mentor_search.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid rgb(223, 194, 107); } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_mentor_search.clicked.connect(self.search_name)#kullanici search butonuna basarak da arama yapabilir
        self.line_mentor_search.returnPressed.connect(self.search_name)#kullanici enter a basinca da arama yapabilir


        self.push_mentor_all_meetings = QtWidgets.QPushButton("All Meetings", parent=self)
        self.push_mentor_all_meetings.setGeometry(QtCore.QRect(320, 110, 81, 21))
        self.push_mentor_all_meetings.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid rgb(223, 194, 107); } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_mentor_all_meetings.clicked.connect(self.show_all_meetings)

        self.push_mentor_back = QtWidgets.QPushButton("Back", parent=self)
        self.push_mentor_back.setGeometry(QtCore.QRect(520, 110, 81, 21))
        self.push_mentor_back.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid rgb(223, 194, 107); } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_mentor_back.clicked.connect(self.go_back)  # Back butonuna fonksiyon bağla

        self.push_mentor_combo_search = QtWidgets.QPushButton("Search", parent=self)
        self.push_mentor_combo_search.setGeometry(QtCore.QRect(520, 155, 81, 21))
        self.push_mentor_combo_search.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid rgb(223, 194, 107); } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_mentor_combo_search.clicked.connect(self.search_combo)  # combo menuden arama yapma butonu

        self.push_mentor_clear = QtWidgets.QPushButton("Clear", parent=self)
        self.push_mentor_clear.setGeometry(QtCore.QRect(420, 110, 81, 21))
        self.push_mentor_clear.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid rgb(223, 194, 107); } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_mentor_clear.clicked.connect(self.clear_table)  # tabloyu temizleme butonu

        self.combo_mentor_dropmenu = QtWidgets.QComboBox(parent=self)
        self.combo_mentor_dropmenu.setGeometry(QtCore.QRect(50, 150, 450, 31))
        self.combo_mentor_dropmenu.setStyleSheet("border-radius: 10px;")
        self.combo_mentor_dropmenu.addItems([
            "VIT projesinin tamamına katılması uygun olur",
            "VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur",
            "VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur",
            "VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.",
            "Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur,",
            "Bir sonraki VIT projesine katilmasi daha uygun olur",
            "Başka bir sektöre yönlendirilmeli",
            "Diger"
        ])
        
        self.push_mentor_exit = QtWidgets.QPushButton("Exit", parent=self)
        self.push_mentor_exit.setGeometry(QtCore.QRect(20, 430, 75, 24))
        self.push_mentor_exit.setStyleSheet("QPushButton { background-color: rgb(209, 0, 0); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_mentor_exit.clicked.connect(self.close)
        
        
        self.tableWidget = QtWidgets.QTableWidget(parent=self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 200, 620, 191))
        self.tableWidget.setStyleSheet("QTableWidget { background-color: white; gridline-color: #D5D8DC; border: 1px solid #BDC3C7; color: black; } QHeaderView::section { background-color: rgb(2, 50, 90); color: white; font: bold 12px 'Tahoma'; border: 1px solid #2980B9; }")
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Meeting Date", "Name Surname", "Mentor", "IT Knowledge", "Intensity", "Comments"])
        self.tableWidget.cellClicked.connect(self.show_comment_details)#uzun comment sutununun okunabilmesi icin

        self.tableWidget.setSortingEnabled(True)
    
        # Filtreleme için üstte bir satır ekle
        self.filter_widgets = []
        self.filter_layout = QHBoxLayout()
        self.filter_widget = QWidget(self)
        self.filter_widget.setGeometry(QtCore.QRect(27, 167, 620, 50))  # Filtre çubuğunu ekle
        
        for col in range(self.tableWidget.columnCount()):
            line_edit = QLineEdit(self)
            line_edit.setPlaceholderText(f"Search {self.tableWidget.horizontalHeaderItem(col).text()}...")
            line_edit.textChanged.connect(lambda _, c=col: self.filter_table(c))
            self.filter_layout.addWidget(line_edit)
            self.filter_widgets.append(line_edit)
        
        self.filter_widget.setLayout(self.filter_layout)


    def go_back(self):
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
    window = MentorMeetingsWindow()
    window.show()
    sys.exit(app.exec())
