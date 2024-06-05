import http.server
import socketserver
Port=9000
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",Port),Handler)as httpd:
    print("Servering at port",Port)
    httpd.serve_forever()