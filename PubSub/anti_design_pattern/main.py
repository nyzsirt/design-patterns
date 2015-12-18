__author__ = 'vivekdogra'

import time

import do


def main():
    """
    synchronous calls to send sms, email, call zoho and DW.
    :return:
    """
    program_start_time = time.time()

    sms_start_time = time.time()
    do.send_sms('9833982602')
    sms_end_time = time.time()
    print("--- SMS took %s seconds ---\n" % (sms_end_time - sms_start_time))

    email_start_time = time.time()
    do.send_email('vivek@credr.com')
    email_end_time = time.time()
    print("--- Email took %s seconds ---\n" % (email_end_time - email_start_time))

    zoho_start_time = time.time()
    do.update_zoho()
    zoho_end_time = time.time()
    print("--- Zoho took %s seconds ---\n" % (zoho_end_time - zoho_start_time))

    dw_start_time = time.time()
    do.push_logs_to_dw()
    dw_end_time = time.time()
    print("--- DW took %s seconds ---\n" % (dw_end_time - dw_start_time))

    program_end_time = time.time()
    print("--- Whole program took %s seconds ---\n" % (program_end_time - program_start_time))


if __name__ == '__main__':
    main()
