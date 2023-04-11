from RMQConsumer import RMQConsumer
from RMQPublisher import RMQPublisher


class RMQConnection:
    def __init__(self):
        self.consumer = RMQConsumer()
        self.publisher = RMQPublisher()
    def start_consume(self):
        self.consumer.start()
    