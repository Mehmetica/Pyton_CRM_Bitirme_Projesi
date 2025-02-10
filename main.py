from PyQt6 import QtWidgets
from login_page import LoginWindow  # Login ekranı için doğru import

import os
# Çalışma dizinini ayarla
os.chdir("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

