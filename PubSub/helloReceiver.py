#!/usr/bin/env python
import pika

# create a connection to message broker
connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))

# open a channel
channel = connection.channel()

# declare a queue
channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exist press CTRL+C'

# declare a function to receive and process messages
def on_message(ch, method, properties, body):
	print " [x] Received %r" % (body,)

# attach a function to receive the message
channel.basic_consume(on_message,
		      queue='hello',
		      no_ack=True)

channel.start_consuming()


