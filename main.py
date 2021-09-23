import json
from http.server import HTTPServer, BaseHTTPRequestHandler

def modification(inp): #Получает, возвращает словарь, не JSON
    return {'answer': sum(inp['summands'])}

class MyHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content = self.rfile.read(int(self.headers['Content-length']))
        print(content)
        print(type(content))
        content = json.loads(content)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        json_response = modification(content)
        self.wfile.write(json.dumps(json_response).encode())

def run(server_class=HTTPServer, handler_class=MyHandler):
    fixed_IP = 'localhost'
    port = 777
    server_address = (fixed_IP, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()