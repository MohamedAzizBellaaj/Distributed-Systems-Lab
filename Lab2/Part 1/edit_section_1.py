import pika

with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
    channel = connection.channel()
    channel.queue_declare(queue="section1")
    updated_text = input("Enter the updated text for section 1: ")
    channel.basic_publish(exchange="", routing_key="section1", body=updated_text)
