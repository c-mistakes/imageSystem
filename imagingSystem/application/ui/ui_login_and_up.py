# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginandup.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_loginAndUp(object):
    def setupUi(self, loginAndUp):
        if not loginAndUp.objectName():
            loginAndUp.setObjectName(u"loginAndUp")
        loginAndUp.resize(757, 544)
        self.verticalLayout_2 = QVBoxLayout(loginAndUp)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.label_3 = QLabel(loginAndUp)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(32)
        font.setBold(False)
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label = QLabel(loginAndUp)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        self.label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label)

        self.username_edit = QLineEdit(loginAndUp)
        self.username_edit.setObjectName(u"username_edit")
        font2 = QFont()
        font2.setPointSize(16)
        self.username_edit.setFont(font2)

        self.horizontalLayout_4.addWidget(self.username_edit)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(loginAndUp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.password_edit = QLineEdit(loginAndUp)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setFont(font2)

        self.horizontalLayout_3.addWidget(self.password_edit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.login_button = QPushButton(loginAndUp)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setFont(font1)

        self.horizontalLayout.addWidget(self.login_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.change_passwd_button = QPushButton(loginAndUp)
        self.change_passwd_button.setObjectName(u"change_passwd_button")
        self.change_passwd_button.setFont(font1)

        self.horizontalLayout.addWidget(self.change_passwd_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(loginAndUp)

        QMetaObject.connectSlotsByName(loginAndUp)
    # setupUi

    def retranslateUi(self, loginAndUp):
        # loginAndUp.setWindowTitle(QCoreApplication.translate("loginAndUp", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("loginAndUp", u"\u6cd5\u533b\u75c5\u7406\u56fe\u50cf\u667a\u80fd\u5904\u7406\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("loginAndUp", u"\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("loginAndUp", u"\u5bc6\u7801", None))
        self.login_button.setText(QCoreApplication.translate("loginAndUp", u"\u767b\u5f55", None))
        self.change_passwd_button.setText(QCoreApplication.translate("loginAndUp", u"\u4fee\u6539\u5bc6\u7801", None))
    # retranslateUi

