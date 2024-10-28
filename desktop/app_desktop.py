import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

from Entity import Task, User


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Task Manager')

        user = self.get_user()

        widget = QLabel(user.username)
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(widget)

    def get_user(self):
        user = User.UserEntity({'username': 'log', 'password': 'log'})
        return user.check_user_db()['user']

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
