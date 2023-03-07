import pika

with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
    channel = connection.channel()
    channel.queue_declare(queue="hello", durable=False)
    channel.basic_publish(exchange="",
                          routing_key="hello",
                          body="Hello World!")
    print(" [x] Sent 'Hello World!'")
