import bcrypt
import cv2
import requests
from PySide6.QtCore import QSize, QRect, QUrl, QUrlQuery, QJsonDocument, QByteArray, Qt
from PySide6.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QSizePolicy, QDialog, QVBoxLayout, \
    QMessageBox
from PySide6 import QtGui, QtCore
from PySide6.QtGui import QImage, QPixmap, QImageReader
import sys
from application.ui.ui_login_and_up import Ui_loginAndUp
from pathlib import Path
import base64
import time


class LoginWindow(QWidget, Ui_loginAndUp):
    def __init__(self, window=None):
        super().__init__()
        self.setWindowTitle("登录")
        self.setupUi(self)
        self.title = QLabel("法医病理图像智能处理系统")

        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button.clicked.connect(self.login)
        self.change_passwd_button.clicked.connect(self.change_passwd)

        self.window = window
        self.setWindowModality(Qt.ApplicationModal)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(300)

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        response = requests.get("http://127.0.0.1:8000/api/login/", params={'username': username, 'password': password})
        if response.status_code == 200:
            data = response.json()
            token = data.get("token")
            print(token)

    def change_passwd(self):
        print(self.password_edit.text())


"""修改密码对话框"""
class ChangePasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("修改密码")

        self.username_label = QLabel("用户名:")
        self.username_edit = QLineEdit()

        self.old_password_label = QLabel("旧密码:")
        self.old_password_edit = QLineEdit()
        self.old_password_edit.setEchoMode(QLineEdit.Password)

        self.new_password_label = QLabel("新密码:")
        self.new_password_edit = QLineEdit()
        self.new_password_edit.setEchoMode(QLineEdit.Password)

        self.confirm_password_label = QLabel("确认新密码:")
        self.confirm_password_edit = QLineEdit()
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)

        self.change_button = QPushButton("修改密码")
        self.change_button.clicked.connect(self.change_password)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.old_password_label)
        layout.addWidget(self.old_password_edit)
        layout.addWidget(self.new_password_label)
        layout.addWidget(self.new_password_edit)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_edit)
        layout.addWidget(self.change_button)

        self.setLayout(layout)

    def change_password(self):
        username = self.username_edit.text()
        old_password = self.old_password_edit.text()
        new_password = self.new_password_edit.text()
        confirm_password = self.confirm_password_edit.text()

        if new_password != confirm_password:
            QMessageBox.warning(self, "错误", "新密码和确认密码不一致！")
            return

        parent = self.parentWidget()

        if parent.verify_credentials(username, old_password):
            hashed_new_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
            credentials = parent.load_credentials()
            credentials[username] = hashed_new_password
            parent.save_credentials(credentials)
            QMessageBox.information(self, "成功", "密码修改成功！")
            self.accept()
        else:
            QMessageBox.warning(self, "错误", "用户名或旧密码错误！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
