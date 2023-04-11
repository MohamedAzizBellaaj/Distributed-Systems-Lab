import pika


class RMQPublisher:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost", heartbeat=0)
        )
        self.channel = self.connection.channel()
