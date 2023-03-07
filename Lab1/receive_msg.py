import pika
import sys
import os


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def main():
    with pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="hello")
        print(" [*] Waiting for messages. To exit press CTRL+C")
        channel.basic_consume(
            queue="hello", on_message_callback=callback, auto_ack=True)
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
