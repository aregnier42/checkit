import http.server
import sys
import os
import socket
import datetime

# simple web app to illustrate kubernetes concepts
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        client=str(self.client_address[0])+" (XFF:"+self.headers.get("X-Forwarded-For","")+")"
        response='['+datetime.datetime.now().strftime("%Y%m%d-%H%M%S.%f")+'] checkit'+' key='+key+' host='+hostname+' - client='+client
        self.wfile.write((response+'\n').encode('utf8'))
        print("==> "+response)

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

print ("starting with..."+str(server_address)+" key="+key+" on "+hostname)
httpd = http.server.HTTPServer(server_address, MyRequestHandler)
httpd.serve_forever()
