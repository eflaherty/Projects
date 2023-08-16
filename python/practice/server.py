import BaseHTTPServer

class simpleHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def respond(self, status, body):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == '/hello':
            self.respond(200, "Hello, world!")
        else:
            self.respond(404, "Unable to find \"%s\"." % self.path)
        return

class simpleServer:
    def __init__(self, host='127.0.0.1', port=8080, handler=simpleHandler):
        self.address = (host, port)
        self.httpd = BaseHTTPServer.HTTPServer(self.address, handler)
    
    def run(self):
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()


if '__main__' == __name__:
    server = simpleServer()
    try:
        print("Starting server - Ctrl-C to stop")
        server.run()
    except KeyboardInterrupt:
        print("\nShutting down server....")
        server.stop()
