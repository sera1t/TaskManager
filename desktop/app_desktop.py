import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

from Entity import Task, User


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Task Manager')
        self.setFixedSize(QSize(500, 302))

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_login = QLineEdit(self.centralwidget)
        self.input_login.setObjectName(u"input_login")
        self.input_login.setGeometry(QRect(171, 85, 133, 22))
        self.input_password = QLineEdit(self.centralwidget)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(171, 135, 133, 22))
        self.Auth_Text = QLabel(self.centralwidget)
        self.Auth_Text.setObjectName(u"Auth_Text")
        self.Auth_Text.setGeometry(QRect(171, 41, 72, 16))
        self.Auth_Text.setStyleSheet(u".QLabel{\n"
                                     "	color: red;\n"
                                     "	font-size: 12px;\n"
                                     "}")
        self.Get_Login = QLabel(self.centralwidget)
        self.Get_Login.setObjectName(u"Get_Login")
        self.Get_Login.setGeometry(QRect(171, 63, 82, 16))
        self.Get_Password = QLabel(self.centralwidget)
        self.Get_Password.setObjectName(u"Get_Password")
        self.Get_Password.setGeometry(QRect(171, 113, 90, 16))
        self.btn_auth = QPushButton(self.centralwidget)
        self.btn_auth.setObjectName(u"btn_auth")
        self.btn_auth.setGeometry(QRect(171, 163, 108, 36))
        self.btn_auth.setStyleSheet(u"QPushButton {\n"
            "	background-color: rgb(255, 253, 253);\n"
            "	border-radius: 5px;\n"
            "	padding: 10px 10px;\n"
            "	color: rgb(55, 107, 113);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "	color: rgb(45, 97, 100);\n"
            "	border: 1px  solid rgb(55, 107, 113);\n"
            "	cursor: pointer;\n"
            "}")
        self.btn_auth.clicked.connect(self.auth)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Task Manager", None))
        self.Auth_Text.setText(QCoreApplication.translate("MainWindow",
                                                          u"Авторизация",
                                                          None))
        self.Get_Login.setText(QCoreApplication.translate("MainWindow",
                                                          u"Введите логин:",
                                                          None))
        self.Get_Password.setText(QCoreApplication.translate("MainWindow",
                                                             u"Введите пароль:",
                                                             None))
        self.btn_auth.setText(QCoreApplication.translate("MainWindow",
                                                         u"Авторизоваться",
                                                         None))

    def auth(self):
        user = User.UserEntity({
            'username': self.input_login.text(),
            'password': self.input_password.text()
        })
        check_user = user.check_user_db()
        if check_user['status']:
            self.statusbar.showMessage('User found')
        else:
            self.statusbar.showMessage('User not found')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
