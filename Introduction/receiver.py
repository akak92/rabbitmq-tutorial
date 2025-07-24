import pika, sys, os
from pika.adapters.blocking_connection import BlockingChannel
from pika import BlockingConnection
import logging

# This script receives messages from a RabbitMQ queue named 'hello'.
# It uses the pika library to connect to RabbitMQ, declare the queue, and consume messages.
# It also sets up basic logging to track the message receiving process.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    connection: BlockingConnection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel: BlockingChannel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        logging.info(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    logging.info(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.info('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)