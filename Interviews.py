from PyQt6 import QtCore, QtGui, QtWidgets

class InterviewsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(680, 467)
        self.setFixedSize(680, 467)

        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(0, -10, 681, 481))
        self.label.setPixmap(QtGui.QPixmap("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/background.jpg"))
        self.label.setScaledContents(True)
        
        self.label_inter_header = QtWidgets.QLabel(parent=self)
        self.label_inter_header.setGeometry(QtCore.QRect(130, 20, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(24)
        self.label_inter_header.setFont(font)
        self.label_inter_header.setStyleSheet("background-color: rgb(223, 194, 107); color: rgb(2, 50, 90); border-radius: 10px; padding: 5px;")
        self.label_inter_header.setText("                      CRM- Interviews")
        
        self.line_inter_search = QtWidgets.QLineEdit(parent=self)
        self.line_inter_search.setGeometry(QtCore.QRect(240, 80, 271, 21))
        self.line_inter_search.setStyleSheet("border-radius: 10px;")

        self.push_inter_search = QtWidgets.QPushButton("Search", parent=self)
        self.push_inter_search.setGeometry(QtCore.QRect(100, 80, 121, 21))
        self.push_inter_search.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid rgb(223, 194, 107); } QPushButton:hover { background-color: rgb(223, 194, 107); }")

        self.push_inter_exit = QtWidgets.QPushButton("Exit", parent=self)
        self.push_inter_exit.setGeometry(QtCore.QRect(590, 430, 75, 24))
        self.push_inter_exit.setStyleSheet("QPushButton { background-color: rgb(209, 0, 0); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.push_inter_exit.clicked.connect(self.close)
        
        self.push_inter_mainmenu = QtWidgets.QPushButton("Main Menu", parent=self)
        self.push_inter_mainmenu.setGeometry(QtCore.QRect(430, 120, 131, 31))
        self.push_inter_mainmenu.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")

        self.frame = QtWidgets.QFrame(parent=self)
        self.frame.setGeometry(QtCore.QRect(50, 140, 601, 271))
        self.frame.setStyleSheet("QFrame { background-color: #F0F0F0; border: 2px solid black; border-radius: 10px; }")

        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 20, 521, 221))
        self.tableWidget_2.setStyleSheet("QTableWidget { background-color: rgb(240, 240, 240); gridline-color: #D5D8DC; border: 1px solid #BDC3C7; } QHeaderView::section { background-color: rgb(2, 50, 90); color: white; font: bold 12px \"Tahoma\"; border: 1px solid #2980B9; }")
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setHorizontalHeaderLabels(["Fullname", "Project Submission Date", "Project Development Date"])
        
        self.push_inter_submited = QtWidgets.QPushButton("Projects Submitted", parent=self)
        self.push_inter_submited.setGeometry(QtCore.QRect(110, 120, 131, 31))
        self.push_inter_submited.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        
        self.push_inter_received = QtWidgets.QPushButton("Projects Received", parent=self)
        self.push_inter_received.setGeometry(QtCore.QRect(270, 120, 131, 31))
        self.push_inter_received.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = InterviewsWindow()
    window.show()
    sys.exit(app.exec())
