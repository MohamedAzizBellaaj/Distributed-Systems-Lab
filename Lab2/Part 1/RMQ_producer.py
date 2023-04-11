import pika


class RMQProducer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost", heartbeat=0)
        )
        self.channel = self.connection.channel()

    def send_message(self, message, queue="", exchange=""):
        return self.channel.basic_publish(
            exchange=exchange, routing_key=queue, body=message
        )
    