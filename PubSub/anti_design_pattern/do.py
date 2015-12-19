__author__ = 'vivekdogra'

import time

def send_sms(number):
    # mimicking sms execution time with sleep method
    time.sleep(1.5)
    print "SMS sent to %r" % number
    return 1

def send_email(email):
    # mimicking email execution time with sleep method
    time.sleep(1)
    print "Email sent to %r" % email
    return 1

def update_zoho():
    # mimicking zoho api call execution time with sleep method
    time.sleep(2)
    print "Zoho updated"
    return 1

def push_logs_to_dw():
    # mimicking dw api call execution time with sleep method
    time.sleep(1)
    print "Logs pushed to DW"
    return 1
