#!/usr/bin/env python
import pika
import time


def publish(message):
    program_start_time = time.time()
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='order_exchange',
                         type='fanout')

    channel.basic_publish(exchange='order_exchange',
                          routing_key='',
                          body=message)
    print " [x] Sent %r" % (message,)
    connection.close()
    program_end_time = time.time()

    print("--- Whole program took %s seconds ---\n" % (program_end_time - program_start_time))


if __name__ == '__main__':
    message = '{"number" : "9833982602", "email" : "vivek.dogra.iitd@gmail.com"}'
    publish(message)
