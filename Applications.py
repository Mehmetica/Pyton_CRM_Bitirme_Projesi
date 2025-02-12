from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication

import sys
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    print(f"Error: {value}")
sys.excepthook = exception_hook

class ApplicationsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(739, 496)

        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(-20, -10, 771, 621))
        self.label.setPixmap(QtGui.QPixmap("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/background.jpg"))
        self.label.setScaledContents(True)

        self.label_app_header = QtWidgets.QLabel(parent=self)
        self.label_app_header.setGeometry(QtCore.QRect(180, 30, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(28)
        self.label_app_header.setFont(font)
        self.label_app_header.setStyleSheet("background-color: rgb(223, 194, 107); color: rgb(2, 50, 90); border-radius: 10px; padding: 5px;")
        self.label_app_header.setText("            CRM- Project Applications")
        
        self.line_app_search = QtWidgets.QLineEdit(parent=self)
        self.line_app_search.setGeometry(QtCore.QRect(20, 120, 151, 31))
        self.line_app_search.setStyleSheet("border-radius: 10px;")
        
        self.push_app_search_2 = QtWidgets.QPushButton("Search", parent=self)
        self.push_app_search_2.setGeometry(QtCore.QRect(20, 160, 151, 31))
        self.push_app_search_2.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid rgb(223, 194, 107); } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        
        self.push_app_search = QtWidgets.QPushButton("All Applications", parent=self)
        self.push_app_search.setGeometry(QtCore.QRect(20, 200, 151, 31))
        self.push_app_search.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        
        self.push_app_planned = QtWidgets.QPushButton("Planned Mentor Meetings", parent=self)
        self.push_app_planned.setGeometry(QtCore.QRect(20, 240, 151, 31))
        self.push_app_planned.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        
        self.push_app_unscheduled = QtWidgets.QPushButton("Unscheduled M. Meetings", parent=self)
        self.push_app_unscheduled.setGeometry(QtCore.QRect(20, 280, 151, 31))
        self.push_app_unscheduled.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        
        self.pushButton_menu = QtWidgets.QPushButton("Main Menu", parent=self)
        self.pushButton_menu.setGeometry(QtCore.QRect(20, 320, 151, 31))
        self.pushButton_menu.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        
        self.pushButton_exit = QtWidgets.QPushButton("Exit", parent=self)
        self.pushButton_exit.setGeometry(QtCore.QRect(30, 460, 75, 24))
        self.pushButton_exit.setStyleSheet("QPushButton { background-color: rgb(209, 0, 0); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.pushButton_exit.clicked.connect(self.close)
        
        self.table_app_anatablo = QtWidgets.QTableWidget(parent=self)
        self.table_app_anatablo.setGeometry(QtCore.QRect(180, 120, 521, 241))
        self.table_app_anatablo.setStyleSheet("QTableWidget { background-color: white; gridline-color: #D5D8DC; border: 1px solid #BDC3C7; } QHeaderView::section { background-color: rgb(2, 50, 90); color: white; font: bold 12px 'Tahoma'; border: 1px solid #2980B9; }")
        self.table_app_anatablo.setRowCount(1)
        self.table_app_anatablo.setColumnCount(7)
        self.table_app_anatablo.setHorizontalHeaderLabels(["Date", "Name Surname", "Mail", "Telephone", "Post Code", "State", "Status"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationsWindow()
    window.show()
    sys.exit(app.exec())
