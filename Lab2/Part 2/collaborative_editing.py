from collaborative_editing_ui import Ui_CollaborativeEditing
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from RMQConnection import RMQConnection


class CollaborativeEditing(QWidget, Ui_CollaborativeEditing):
    update_value = QtCore.Signal(str)

    def __init__(self, connection: RMQConnection):
        super().__init__()
        self.section1 = ""
        self.section2 = ""
        self.setupUi(self)
        self.setWindowTitle("Collaborative Editing")
        self.connection = connection
        self.connection.consumer.declare_queue(queue="section1")
        self.connection.consumer.declare_queue(queue="section2")
        self.connection.consumer.listen_queue(queue="section1", callback=self.callback_section_1)
        self.connection.consumer.listen_queue(queue="section2", callback=self.callback_section_2)
        self.connection.start_consume()
    def callback_section_1(self, ch, method, properties, body):
        self.section1 = str(body, "utf-8")
        self.text_area.setText("Updated 1")
        self.test()

    def callback_section_2(self, ch, method, properties, body):
        self.section2 = str(body, "utf-8")
        self.text_area.setText("Updated 2")
        self.test()

    def test(self):
        print(
            f"""
              Section 1 : {self.section1}
              Section 2 : {self.section2}
              """
        )