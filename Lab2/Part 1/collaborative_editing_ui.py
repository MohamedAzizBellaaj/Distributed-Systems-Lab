# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collaborative_editing.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)


class Ui_CollaborativeEditing(object):
    def setupUi(self, CollaborativeEditing):
        if not CollaborativeEditing.objectName():
            CollaborativeEditing.setObjectName("CollaborativeEditing")
        CollaborativeEditing.resize(499, 300)
        self.verticalLayout_2 = QVBoxLayout(CollaborativeEditing)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(CollaborativeEditing)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.section_number = QLineEdit(CollaborativeEditing)
        self.section_number.setObjectName("section_number")

        self.horizontalLayout.addWidget(self.section_number)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.section_edit_area = QTextEdit(CollaborativeEditing)
        self.section_edit_area.setObjectName("section_edit_area")

        self.verticalLayout.addWidget(self.section_edit_area)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.text_area = QTextEdit(CollaborativeEditing)
        self.text_area.setObjectName("text_area")

        self.horizontalLayout_2.addWidget(self.text_area)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.edit_button = QPushButton(CollaborativeEditing)
        self.edit_button.setObjectName("edit_button")

        self.verticalLayout_2.addWidget(self.edit_button)

        self.retranslateUi(CollaborativeEditing)

        QMetaObject.connectSlotsByName(CollaborativeEditing)

    # setupUi

    def retranslateUi(self, CollaborativeEditing):
        CollaborativeEditing.setWindowTitle(
            QCoreApplication.translate("CollaborativeEditing", "Form", None)
        )
        self.label.setText(
            QCoreApplication.translate("CollaborativeEditing", "Section:", None)
        )
        self.edit_button.setText(
            QCoreApplication.translate("CollaborativeEditing", "Edit", None)
        )

    # retranslateUi
