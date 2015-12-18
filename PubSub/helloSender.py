#!/usr/bin/env python
import pika

# create a connection to message broker
connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))

# open a channel
channel = connection.channel()

# declare a queue
channel.queue_declare(queue='hello')

# compose a message
#message = "Hello, World!"

# a json object
message = '{"name" : "Vivek"}'

# publish a message with body 'Hello, World' to the queue 'hello'
channel.basic_publish(exchange='',
		      routing_key='hello',
		      body=message)

print " [x] Sent %r" % message
connection.close()
