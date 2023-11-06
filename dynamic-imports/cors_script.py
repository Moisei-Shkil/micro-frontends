cors_server_script = """
import http.server
import socketserver

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Type", "text/html")
        http.server.SimpleHTTPRequestHandler.end_headers(self)

with socketserver.TCPServer(('localhost', {port}), CORSRequestHandler) as httpd:
    print(f'Serving on port {port}...')
    httpd.serve_forever()
"""
