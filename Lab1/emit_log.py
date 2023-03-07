import pika
import sys


EXCHANGE_NAME = "direct"
with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
    channel = connection.channel()
    channel.exchange_declare(EXCHANGE_NAME, exchange_type="direct")
    argv = sys.argv[1].split(":")
    severity = argv[0]
    message = argv[1]
    channel.basic_publish(exchange=EXCHANGE_NAME,
                          routing_key=severity,
                          body=message)
    print(f" [x] Sent '{severity}:{message}'")
