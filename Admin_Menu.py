from PyQt6 import QtCore, QtGui, QtWidgets
# from login_page import LoginWindow


class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(682, 411)
        self.setFixedSize(682, 411)

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(-20, -10, 711, 431))
        self.label.setPixmap(QtGui.QPixmap("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/diger_dosyalar/background.jpg"))
        self.label.setScaledContents(True)

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(20, 140, 641, 221))
        self.frame.setStyleSheet("QFrame { background-color: #F0F0F0; border: 2px solid black; border-radius: 10px; }")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 20, 621, 191))
        self.tableWidget_2.setStyleSheet("QTableWidget { background-color: rgb(240, 240, 240); gridline-color: #D5D8DC; border: 1px solid #BDC3C7; }")
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(4)

        self.label_admin_header = QtWidgets.QLabel(parent=Form)
        self.label_admin_header.setGeometry(QtCore.QRect(150, 30, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(28)
        self.label_admin_header.setFont(font)
        self.label_admin_header.setStyleSheet("background-color: rgb(223, 194, 107); color: rgb(2, 50, 90); border-radius: 10px; padding: 5px;")
        self.label_admin_header.setText("Admin Menu")

        self.push_admin_mail = QtWidgets.QPushButton(parent=Form)
        self.push_admin_mail.setGeometry(QtCore.QRect(270, 100, 151, 31))
        self.push_admin_mail.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_admin_mail.setText("Mail")

        self.push_admin_menu = QtWidgets.QPushButton(parent=Form)
        self.push_admin_menu.setGeometry(QtCore.QRect(470, 100, 151, 31))
        self.push_admin_menu.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_admin_menu.setText("Main Menu")

        self.push_admin_event = QtWidgets.QPushButton(parent=Form)
        self.push_admin_event.setGeometry(QtCore.QRect(60, 100, 151, 31))
        self.push_admin_event.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_admin_event.setText("Event Registration")

        self.push_admin_exit = QtWidgets.QPushButton(parent=Form)
        self.push_admin_exit.setGeometry(QtCore.QRect(10, 370, 75, 24))
        self.push_admin_exit.setStyleSheet("QPushButton { background-color: rgb(209, 0, 0); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_admin_exit.setText("Exit")

class AdminMenuWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.stacked_widget = stacked_widget  # Sayfa yönetimi için stacked widget bağlantısı

        # Buton işlevlerini bağlama
        self.push_admin_mail.clicked.connect(self.open_mail)
        self.push_admin_menu.clicked.connect(self.open_main_menu)
        self.push_admin_event.clicked.connect(self.open_event_registration)
        self.push_admin_exit.clicked.connect(self.exit_application)

    def open_mail(self):
        QtWidgets.QMessageBox.information(self, "Mail", "Opening Mail Interface...")

    def open_main_menu(self):
        QtWidgets.QMessageBox.information(self, "Main Menu", "Returning to Main Menu...")

    def open_event_registration(self):
        QtWidgets.QMessageBox.information(self, "Event Registration", "Opening Event Registration...")

    def exit_application(self):
        from login_page import LoginWindow
        self.close()
        self.login_window= LoginWindow()
        self.login_window.show()
        # self.stacked_widget.setCurrentIndex(0)  # Login sayfasına geçiş

# Debug için doğrudan çalıştırılabilir
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_menu = AdminMenuWindow()
    admin_menu.show()
    sys.exit(app.exec())
