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

    def listen_queue(self, queue, callback, **args):
        return self.channel.basic_consume(
            queue=queue, on_message_callback=callback, **args
        )

    def send_ack(self, tag):
        self.channel.basic_ack(tag)
