from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow

from collaborative_editing_ui_final import Ui_CollaborativeEditingFinal
from RMQ_connection import RMQConnection


class CollaborativeEditing(Ui_CollaborativeEditingFinal):
    update_text_area = QtCore.Signal()

    def __init__(self, connection: RMQConnection):
        super().__init__(connection)
        self.main_window = QMainWindow()
        self.setupUi(self.main_window)
        self.section1_edit_area.textChanged.connect(self.update_text_area_slot)
        self.section2_edit_area.textChanged.connect(self.update_text_area_slot)
        self.connection.start_consume()

    def show(self):
        self.main_window.show()

    def update_text_area_slot(self):
        self.whole_text.setText(f"{self.section1_edit_area.toPlainText()}\n{self.section2_edit_area.toPlainText()}")
