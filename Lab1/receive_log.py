import pika
import sys
import os


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


EXCHANGE_NAME = "direct"


def main():
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.exchange_declare(EXCHANGE_NAME)
        if (len(sys.argv) < 2):
            print("Usage: receive_logs.py [info] [warning] [error]")
            exit()
        queue = channel.queue_declare("").method.queue
        for severity in sys.argv[1:]:
            channel.queue_bind(queue, EXCHANGE_NAME, severity)
        print(" [*] Waiting for messages. To exit press CTRL+C")
        channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            raise
