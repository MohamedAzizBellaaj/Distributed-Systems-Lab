import threading

import pika


class RMQConsumer(threading.Thread):
    def __init__(self):
        super(RMQConsumer, self).__init__()
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost", heartbeat=0)
        )
        self.channel = self.connection.channel()

    def run(self):
        threading.Thread(target=self.channel.start_consuming, daemon=True).start()

    def declare_queue(self, queue, **args):
        name = self.channel.queue_declare(queue=queue, **args)
        return name.method.queue

    def declare_exchange(self, exchange, type):
        return self.channel.exchange_declare(exchange=exchange, exchange_type=type)

    def bind_queue_exchange(self, queue, exchange):
        return self.channel.queue_bind(exchange=exchange, queue=queue)

    def send_message(self, message, queue="", exchange=""):
        return self.channel.basic_publish(
            exchange=exchange, routing_key=queue, body=message
        )

    def send_ack(self, tag):
        self.channel.basic_ack(tag)

    def listen_queue(self, queue, callback, **args):
        return self.channel.basic_consume(
            queue=queue, on_message_callback=callback, **args
        )
