from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMenuBar,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from edit_section_text_area import EditSectionTextArea
from RMQ_connection import RMQConnection


class Ui_CollaborativeEditingFinal(object):
    def __init__(self, connection: RMQConnection):
        self.connection = connection

    def setupUi(self, CollaborativeEditing):
        if not CollaborativeEditing.objectName():
            CollaborativeEditing.setObjectName("CollaborativeEditing")
        CollaborativeEditing.resize(664, 505)
        self.centralwidget = QWidget(CollaborativeEditing)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(0, 10, 584, 462))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.section1_label = QLabel(self.widget)
        self.section1_label.setObjectName("section1_label")

        self.horizontalLayout.addWidget(self.section1_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.section1_edit_area = EditSectionTextArea(self.widget, self.connection, 1)
        self.section1_edit_area.setObjectName("section1_edit_area")

        self.verticalLayout.addWidget(self.section1_edit_area)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.section2_label = QLabel(self.widget)
        self.section2_label.setObjectName("section2_label")

        self.horizontalLayout_2.addWidget(self.section2_label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.section2_edit_area = EditSectionTextArea(self.widget, self.connection, 2)
        self.section2_edit_area.setObjectName("section2_edit_area")

        self.verticalLayout_2.addWidget(self.section2_edit_area)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.whole_text = QTextEdit(self.widget)
        self.whole_text.setObjectName("whole_text")

        self.horizontalLayout_3.addWidget(self.whole_text)

        CollaborativeEditing.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CollaborativeEditing)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 664, 22))
        CollaborativeEditing.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CollaborativeEditing)
        self.statusbar.setObjectName("statusbar")
        CollaborativeEditing.setStatusBar(self.statusbar)

        self.retranslateUi(CollaborativeEditing)

        QMetaObject.connectSlotsByName(CollaborativeEditing)

    def retranslateUi(self, CollaborativeEditing):
        CollaborativeEditing.setWindowTitle(
            QCoreApplication.translate("CollaborativeEditing", "MainWindow", None)
        )
        self.section1_label.setText(
            QCoreApplication.translate("CollaborativeEditing", "Section 1:", None)
        )
        self.section2_label.setText(
            QCoreApplication.translate("CollaborativeEditing", "Section 2:", None)
        )
