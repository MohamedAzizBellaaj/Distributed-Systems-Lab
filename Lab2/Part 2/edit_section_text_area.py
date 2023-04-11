import json

from PySide6 import QtCore, QtWidgets

from RMQ_connection import RMQConnection


class EditSectionTextArea(QtWidgets.QTextEdit):
    update_value = QtCore.Signal(str)
    update_text_area = QtCore.Signal()

    def __init__(
        self,
        widget: QtWidgets.QWidget,
        connection: RMQConnection,
        index: int,
    ):
        super(EditSectionTextArea, self).__init__(widget)
        self.index = index
        self.connection = connection
        self.identifier = f"section{self.index}_edit_area"
        self.exchange = f"exchange.{self.identifier}"
        self.update_queue = f"{self.connection.client_id}.{self.identifier}"
        self.last_updated_value = ""

        self.setObjectName(self.identifier)
        self.update_value.connect(self.setText)

        self.connection.publisher.queue_declare(
            self.identifier, arguments={"x-max-length": 1}
        )

        self.connection.publisher.declare_bind_queue_exchange(
            self.update_queue, self.exchange
        )
        self.connection.consumer.listen_queue(self.update_queue, self.on_edit_request)

    def on_edit_request(self, ch, method, properties, body):
        delivery_tag = method.delivery_tag
        payload = json.loads(body)
        if "index" not in payload or "message" not in payload:
            return
        if payload["index"] != self.index:
            return
        self.clearFocus()
        self.update_value.emit(payload["message"])
        self.connection.consumer.send_ack(delivery_tag)

    def edit_request_lock(self):
        payload = {"user": self.connection.client_id}
        self.connection.publisher.send_message(
            queue=self.identifier, message=json.dumps(payload)
        )

    def focusInEvent(self, e):
        super(EditSectionTextArea, self).focusInEvent(e)
        self.edit_request_lock()

    def focusOutEvent(self, e):
        super(EditSectionTextArea, self).focusOutEvent(e)
        if self.last_updated_value == self.toPlainText():
            return
        payload = {"message": self.toPlainText(), "index": self.index}
        self.connection.publisher.send_message(
            exchange=self.exchange, message=json.dumps(payload)
        )
        self.last_updated_value = self.toPlainText()