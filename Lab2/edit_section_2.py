import pika

with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
    channel = connection.channel()
    channel.queue_declare(queue="section2")
    updated_text = input("Enter the updated text for section 2: ")
    channel.basic_publish(
        exchange="",
        routing_key="section2",
        body=updated_text
    )
    print("Waiting for updates...")
