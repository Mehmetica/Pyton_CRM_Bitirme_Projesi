# Form implementation generated from reading ui file '/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 410)
        Dialog.setMinimumSize(QtCore.QSize(531, 410))
        Dialog.setMaximumSize(QtCore.QSize(531, 410))
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 0, 541, 411))
        self.label.setStyleSheet("background-image: url(\"background.jpg\"); \n"
"background-repeat: no-repeat; \n"
"background-position: center; \n"
"background-size: cover;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(60, 80, 421, 251))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #F0F0F0; /* Açık gri arka plan */\n"
"    border: 2px solid black; /* Siyah kenarlık */\n"
"    border-radius: 10px; /* Yuvarlatılmış köşeler */\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.push_admin_Applications = QtWidgets.QPushButton(parent=self.frame)
        self.push_admin_Applications.setGeometry(QtCore.QRect(70, 120, 111, 61))
        self.push_admin_Applications.setStyleSheet("QPushButton {\n"
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
        self.push_admin_Applications.setObjectName("push_admin_Applications")
        self.push_admin_mentorMeeting = QtWidgets.QPushButton(parent=self.frame)
        self.push_admin_mentorMeeting.setGeometry(QtCore.QRect(240, 50, 111, 61))
        self.push_admin_mentorMeeting.setStyleSheet("QPushButton {\n"
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
        self.push_admin_mentorMeeting.setObjectName("push_admin_mentorMeeting")
        self.push_admin_interviews = QtWidgets.QPushButton(parent=self.frame)
        self.push_admin_interviews.setGeometry(QtCore.QRect(70, 50, 111, 61))
        self.push_admin_interviews.setStyleSheet("QPushButton {\n"
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
        self.push_admin_interviews.setObjectName("push_admin_interviews")
        self.push_admin_exit = QtWidgets.QPushButton(parent=self.frame)
        self.push_admin_exit.setGeometry(QtCore.QRect(160, 210, 111, 31))
        self.push_admin_exit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(211, 0, 0); /* Yeşil arka plan */\n"
"    color: white; /* Beyaz yazı */\n"
"    border-radius: 10px; /* Yuvarlak köşeler */\n"
"    border: 2px solid #000000; /* Siyah kenarlık */\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
"}")
        self.push_admin_exit.setObjectName("push_admin_exit")
        self.push_admin_adminmenu = QtWidgets.QPushButton(parent=self.frame)
        self.push_admin_adminmenu.setGeometry(QtCore.QRect(240, 120, 111, 61))
        self.push_admin_adminmenu.setStyleSheet("QPushButton {\n"
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
        self.push_admin_adminmenu.setObjectName("push_admin_adminmenu")
        self.label_admin_header = QtWidgets.QLabel(parent=Dialog)
        self.label_admin_header.setGeometry(QtCore.QRect(100, 60, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(20)
        self.label_admin_header.setFont(font)
        self.label_admin_header.setStyleSheet("background-color: rgb(223, 194, 107);  /* Arka plan rengi */\n"
"color: rgb(2, 50, 90);  /* Yazı rengi */\n"
"border-radius: 10px;  /* Köşeleri yuvarlat */\n"
"padding: 5px;  /* Buton içindeki boşluk */")
        self.label_admin_header.setObjectName("label_admin_header")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.push_admin_Applications.setText(_translate("Dialog", "Applications"))
        self.push_admin_mentorMeeting.setText(_translate("Dialog", "Mentor Meeting"))
        self.push_admin_interviews.setText(_translate("Dialog", "Interviews"))
        self.push_admin_exit.setText(_translate("Dialog", "Exit"))
        self.push_admin_adminmenu.setText(_translate("Dialog", "Admin Menu"))
        self.label_admin_header.setText(_translate("Dialog", "        CRM- Admin Prefence Menu"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Dialog()
    window.show()
    sys.exit(app.exec())
