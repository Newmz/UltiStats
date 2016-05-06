#we use this to start the webpage.

import SimpleHTTPServer
import SocketServer
import webbrowser
import sys
PORT = 8080

if len(sys.argv)>1:
	PORT = int(sys.argv[1])

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
webbrowser.open("http://localhost:" + str(PORT) + "/demo.html")
httpd.serve_forever()
