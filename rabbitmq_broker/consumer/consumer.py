import pika
import time

time.sleep(8)  # wait a bit for RabbitMQ but be faster than producer

connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()

channel.queue_declare(queue="hello", durable=True)

def callback(ch, method, properties, body):
    print("Received:", body.decode())

channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

print("Waiting for messages...")
channel.start_consuming()
