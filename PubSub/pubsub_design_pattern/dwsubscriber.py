#!/usr/bin/env python
import pika
import time


def subscribe():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='order_exchange',
                             type='fanout')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='order_exchange',
                       queue=queue_name)

    print ' [*] Waiting for message. To exit press CTRL+C'

    def on_message_push_logs_to_dw(ch, method, properties, body):
        # mimicking dw api call execution time with sleep method
        time.sleep(1)
        print "Logs pushed to DW"
        return 1

    channel.basic_consume(on_message_push_logs_to_dw,
                          queue=queue_name,
                          no_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    subscribe()
