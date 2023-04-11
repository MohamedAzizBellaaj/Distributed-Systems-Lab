import uuid

from RMQ_consumer import RMQConsumer
from RMQ_publisher import RMQPublisher


class RMQConnection:
    def __init__(self):
        self.client_id = str(uuid.uuid4())
        self.consumer = RMQConsumer()
        self.publisher = RMQPublisher()

    def start_consume(self):
        self.consumer.start()
