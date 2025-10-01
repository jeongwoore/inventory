# login_dialog.py
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from db_helper import DB

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.db = DB()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.user_label = QLabel("Username:")
        self.user_input = QLineEdit()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)

        self.pass_label = QLabel("Password:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.pass_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.try_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def try_login(self):
        # 최소 예제에서는 로그인 검증 없이 통과
        self.accept()
