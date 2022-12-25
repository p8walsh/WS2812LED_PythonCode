import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the request body
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        # Parse the request body as JSON
        data = json.loads(body)

        # Print the list of tuples to the console
        print(data)
        list_of_rgb = [(dictionary['r'], dictionary['g'], dictionary['b']) for dictionary in data]
        print(list_of_rgb)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

# Start the server on port 8000
server = HTTPServer(('', 8000), RequestHandler)
server.serve_forever()
