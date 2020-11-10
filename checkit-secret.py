import BaseHTTPServer
import SimpleHTTPServer
import sys
import os
import socket
import datetime
# simple web app to illustrate kubernetes concepts (v2)
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        client=str(self.headers.get("X-Forwarded-For","n/a"))+" - " +str(self.client_address[0])
        response='['+datetime.datetime.now().strftime("%Y%m%d-%H%M%S.%f")+']'+b' key='+key+b' host='+hostname+b' [sec='+secret[:2]+b'...] - Hello '+client+' \n'
        self.wfile.write(response)
        print("==> "+response)
        print(self.headers)
if sys.argv[2:]:
    port = int(sys.argv[1])
    key = str(sys.argv[2])
else:
    port=int(os.getenv('CHECKIT_PORT', 8080))
    key=os.getenv('CHECKIT_KEY',"n/a")
server_address = ('0.0.0.0', port)
hostname=socket.gethostname()
if len(hostname)>5:
    hostname=hostname[-5:]
print "reading secret..."
secret="?"
if os.path.isfile('/config/checkit/checkit.conf'):
    try:
        fp = open('/config/checkit/checkit.conf')
        secret=fp.readline()
    finally:
        fp.close()
print "starting with..."+str(server_address)+" key="+key+" sec="+secret[:2]+"... on " +hostname
httpd = BaseHTTPServer.HTTPServer(server_address, MyRequestHandler)
httpd.serve_forever()
