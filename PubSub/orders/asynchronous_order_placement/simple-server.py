#!/usr/bin/env python
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

from PubSub.anti_design_pattern import do

PORT = 8003
FILE_PREFIX = "."

if __name__ == "__main__":
    try:
        import argparse

        parser = argparse.ArgumentParser(description='A simple server for testing.')
        parser.add_argument('-p', '--port', type=int, dest="PORT",
                           help='the port to run the server on; defaults to 8003')
        parser.add_argument('--path', type=str, dest="PATH",
                           help='the folder to find the json files')

        args = parser.parse_args()

        if args.PORT:
            PORT = args.PORT
        if args.PATH:
            FILE_PREFIX = args.PATH

    except Exception:
        # Could not successfully import argparse or something
        pass


class HTTPRequestHandler (BaseHTTPRequestHandler):

    def do_GET(self):

        #send response code:
        self.send_response(200)
        #send headers:
        self.send_header("Content-type", "text/html")
        # send a blank line to end headers:
        self.wfile.write("\n")

        try:
            output = open('async.html').read()
        except Exception:
            output = "{'error': 'Could not find index file'}"
        self.wfile.write(output)

    def do_POST(self):
        if self.path == "/reserve/bike/":
            response_code = 200
        elif self.path == "/error":
            response_code = 500
        else:
            try:
                response_code = int(self.path[1:])
            except Exception:
                response_code = 201
            
        try:
            self.send_response(response_code)
            self.wfile.write('Content-Type: application/json\n')
            self.wfile.write('Client: %s\n' % str(self.client_address))
            self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
            self.wfile.write('Path: %s\n' % self.path)

            self.end_headers()


            form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD':'POST',
                                     'CONTENT_TYPE':self.headers['Content-Type'],
                                     })
            number = ''
            email = ''
            do.send_sms(number)
            do.send_email(email)
            do.update_zoho()
            do.push_logs_to_dw()
            self.wfile.write('{\n')

            self.wfile.write('\n}')

        except Exception as e:
            self.send_response(500)


server = HTTPServer(("localhost", PORT), HTTPRequestHandler)
server.serve_forever()
