import threading

import pika
from collaborative_editing import CollaborativeEditing


class Consumer(CollaborativeEditing):
    def __init__(self):
        super().__init__()
        self.section1 = ""
        self.section2 = ""
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost", heartbeat=0)
        )
        self.channel = self.connection.channel()
        self.consuming_thread = None

    def consume(self):
        self.channel.basic_consume(
            queue="section1", on_message_callback=self.callback_section_1, auto_ack=True
        )
        self.channel.basic_consume(
            queue="section2", on_message_callback=self.callback_section_2, auto_ack=True
        )
        self.channel.start_consuming()

    def start_consuming_threads(self):
        self.consuming_thread = threading.Thread(target=self.consume)
        self.consuming_thread.start()

    def callback_section_1(self, ch, method, properties, body):
        self.section1 = str(body, "utf-8")
        self.section_edit_area.setText("Updated")
        self.test()

    def callback_section_2(self, ch, method, properties, body):
        self.section2 = str(body, "utf-8")
        self.section_edit_area.setText("Updated")
        self.test()

    def test(self):
        print(
            f"""
              Section 1 : {self.section1}
              Section 2 : {self.section2}
              """
        )
