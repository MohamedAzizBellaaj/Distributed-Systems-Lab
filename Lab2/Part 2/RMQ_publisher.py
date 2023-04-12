import pika
from pika.exchange_type import ExchangeType


class RMQPublisher:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost", heartbeat=0)
        )
        self.channel = self.connection.channel()

    def send_message(self, message, queue="", exchange=""):
        return self.channel.basic_publish(
            exchange=exchange, routing_key=queue, body=message
        )

    def declare_bind_queue_exchange(self, queue, exchange):
        self.queue_declare(queue=queue, durable=True)
        self.exchange_declare(exchange=exchange, exchange_type=ExchangeType.fanout)
        self.bind_queue_exchange(exchange=exchange, queue=queue)

    def queue_declare(self, queue, **args):
        name = self.channel.queue_declare(queue=queue, durable=True, **args)
        return name.method.queue

    def exchange_declare(self, exchange, exchange_type):
        return self.channel.exchange_declare(
            exchange=exchange, exchange_type=exchange_type
        )
    def queue_delete(self, queue):
        self.channel.queue_delete(queue=queue)

    def bind_queue_exchange(self, queue, exchange):
        return self.channel.queue_bind(exchange=exchange, queue=queue)
