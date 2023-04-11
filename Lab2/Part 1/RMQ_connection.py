from RMQ_consumer import RMQConsumer
from RMQ_producer import RMQProducer


class RMQConnection:
    def __init__(self):
        self.consumer = RMQConsumer()
        self.producer = RMQProducer()

    def start_consume(self):
        self.consumer.start()
