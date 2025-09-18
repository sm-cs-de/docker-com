import pika
import time

time.sleep(10)  # wait a bit for RabbitMQ to start

connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()

# declare a queue
channel.queue_declare(queue="hello", durable=True)

# send a message
channel.basic_publish(exchange="", routing_key="hello", body="Hello from Producer!", properties = pika.BasicProperties(delivery_mode=2))
print("Sent: Hello from Producer!")

connection.close()

