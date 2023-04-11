# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collaborative_editing.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_CollaborativeEditing(object):
    def setupUi(self, CollaborativeEditing):
        if not CollaborativeEditing.objectName():
            CollaborativeEditing.setObjectName(u"CollaborativeEditing")
        CollaborativeEditing.resize(664, 505)
        self.centralwidget = QWidget(CollaborativeEditing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 584, 462))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.section1_label = QLabel(self.widget)
        self.section1_label.setObjectName(u"section1_label")

        self.horizontalLayout.addWidget(self.section1_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.section1_edit_area = QTextEdit(self.widget)
        self.section1_edit_area.setObjectName(u"section1_edit_area")

        self.verticalLayout.addWidget(self.section1_edit_area)

        self.section1_button = QPushButton(self.widget)
        self.section1_button.setObjectName(u"section1_button")

        self.verticalLayout.addWidget(self.section1_button)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.section2_label = QLabel(self.widget)
        self.section2_label.setObjectName(u"section2_label")

        self.horizontalLayout_2.addWidget(self.section2_label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.section2_edit_area = QTextEdit(self.widget)
        self.section2_edit_area.setObjectName(u"section2_edit_area")

        self.verticalLayout_2.addWidget(self.section2_edit_area)

        self.section2_button = QPushButton(self.widget)
        self.section2_button.setObjectName(u"section2_button")

        self.verticalLayout_2.addWidget(self.section2_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.whole_text = QTextEdit(self.widget)
        self.whole_text.setObjectName(u"whole_text")

        self.horizontalLayout_3.addWidget(self.whole_text)

        CollaborativeEditing.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CollaborativeEditing)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 664, 22))
        CollaborativeEditing.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CollaborativeEditing)
        self.statusbar.setObjectName(u"statusbar")
        CollaborativeEditing.setStatusBar(self.statusbar)

        self.retranslateUi(CollaborativeEditing)

        QMetaObject.connectSlotsByName(CollaborativeEditing)
    # setupUi

    def retranslateUi(self, CollaborativeEditing):
        CollaborativeEditing.setWindowTitle(QCoreApplication.translate("CollaborativeEditing", u"MainWindow", None))
        self.section1_label.setText(QCoreApplication.translate("CollaborativeEditing", u"Section 1:", None))
        self.section1_button.setText(QCoreApplication.translate("CollaborativeEditing", u"Done", None))
        self.section2_label.setText(QCoreApplication.translate("CollaborativeEditing", u"Section 2:", None))
        self.section2_button.setText(QCoreApplication.translate("CollaborativeEditing", u"Done", None))
    # retranslateUi

