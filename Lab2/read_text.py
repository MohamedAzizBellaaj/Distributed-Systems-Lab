import os
import sys
import pika

section1 = ""
section2 = ""


def callback_section_1(ch, method, properties, body):
    global section1
    section1 = str(body)
    print(f"Section 1 : {section1}")
    print(f"Section 2 : {section2}")


def callback_section_2(ch, method, properties, body):
    global section2
    section2 = str(body)
    print(f"Section 1 : {section1}")
    print(f"Section 2 : {section2}")


def main():
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.basic_consume(
            queue="section1", on_message_callback=callback_section_1, auto_ack=True)
        channel.basic_consume(
            queue="section2", on_message_callback=callback_section_2, auto_ack=True)
        channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            raise
