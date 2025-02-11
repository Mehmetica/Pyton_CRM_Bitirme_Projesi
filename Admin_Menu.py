from PyQt6 import QtWidgets

class AdminMenuWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Pencere başlığı
        self.setWindowTitle("Admin Menu")

        # Pencere boyutları
        self.resize(600, 400)

        # Layout ve bileşenler
        layout = QtWidgets.QVBoxLayout()

        # Örnek butonlar
        self.push_admin_mail = QtWidgets.QPushButton("Open Mail")
        self.push_admin_menu = QtWidgets.QPushButton("Main Menu")
        self.push_admin_event = QtWidgets.QPushButton("Event Registration")
        self.push_admin_exit = QtWidgets.QPushButton("Exit")

        # Butonları layout'a ekleme
        layout.addWidget(self.push_admin_mail)
        layout.addWidget(self.push_admin_menu)
        layout.addWidget(self.push_admin_event)
        layout.addWidget(self.push_admin_exit)

        # Layout'u pencereye ayarlama
        self.setLayout(layout)

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
        QtWidgets.QApplication.quit()


# Debug için doğrudan çalıştırılabilir
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_menu = AdminMenuWindow()
    admin_menu.show()
    sys.exit(app.exec())
