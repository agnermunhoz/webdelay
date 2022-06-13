from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        #time.sleep(60)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Delay</head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Web server with delay.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    print("Server started http://%s:%s" % (hostName, serverPort))
    webServer = HTTPServer((hostName, serverPort), MyServer)

    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        print("Server started http://%s:%s" % (hostName, serverPort))
        webServer.serve_forever()
        print("Server started http://%s:%s" % (hostName, serverPort))
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
