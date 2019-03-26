import BaseHTTPServer
import SimpleHTTPServer
import sys
import os
import socket
import datetime

# simple web app to illustrate kubernetes concepts
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response=b'['+datetime.datetime.now().strftime("%Y%m%d-%H%M%S.%f")+']'+b' key='+key+b' host='+hostname+b' - Hello '+str(self.client_address[0])+' \n'     
        self.wfile.write(response)
        print("==> "+response)

if sys.argv[2:]:
    port = int(sys.argv[1])
    key = str(sys.argv[2])
else:
    print "syntax: 'checkit <port> <key>' with port number for server and arbitrary key value"
    sys.exit(1)

server_address = ('0.0.0.0', port)
hostname=socket.gethostname()
if len(hostname)>5:
    hostname=hostname[-5:]

print "starting with..."+str(server_address)+" key="+key+" on "+hostname
httpd = BaseHTTPServer.HTTPServer(server_address, MyRequestHandler)
httpd.serve_forever()
