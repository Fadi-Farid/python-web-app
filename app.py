# file: server.py
from http.server import HTTPServer, CGIHTTPRequestHandler
server = HTTPServer(('localhost', 8000), CGIHTTPRequestHandler)
print('Starting server at localhost:8000.')
server.serve_forever()
