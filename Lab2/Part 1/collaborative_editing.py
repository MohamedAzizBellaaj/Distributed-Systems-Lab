from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from collaborative_editing_ui import Ui_CollaborativeEditing
from RMQ_connection import RMQConnection


class CollaborativeEditing(QWidget, Ui_CollaborativeEditing):
    update_text_area = QtCore.Signal()

    def __init__(self, connection: RMQConnection):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Collaborative Editing")
        self.section1 = ""
        self.section2 = ""
        self.connection = connection
        self.connection.consumer.queue_declare(queue="section1")
        self.connection.consumer.queue_declare(queue="section2")
        self.connection.consumer.listen_queue(
            queue="section1", callback=self.callback_section_1
        )
        self.connection.consumer.listen_queue(
            queue="section2", callback=self.callback_section_2
        )
        self.section_edit_area.textChanged.connect(self.on_text_edit)
        self.update_text_area.connect(self.update_text_area_slot)
        self.connection.start_consume()

    def callback_section_1(self, ch, method, properties, body):
        self.section1 = str(body, "utf-8")
        self.update_text_area.emit()

    def callback_section_2(self, ch, method, properties, body):
        self.section2 = str(body, "utf-8")
        self.update_text_area.emit()

    def on_text_edit(self):
        section_number = self.section_number.text()
        if section_number:
            self.connection.producer.send_message(
                self.section_edit_area.toPlainText(), queue=f"section{section_number}"
            )

    def update_text_area_slot(self):
        self.text_area.setText(f"{self.section1}\n{self.section2}")
