import pika
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel
import logging

# This script sends a message to a RabbitMQ queue named 'hello'.
# It uses the pika library to connect to RabbitMQ, declare the queue, and publish a message.
# It also sets up basic logging to track the message sending process.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

connection: BlockingConnection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel: BlockingChannel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

logging.info(" [x] Sent 'Hello World!'")

connection.close()