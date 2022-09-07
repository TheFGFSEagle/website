#!/usr/bin/python
import http.server

s = http.server.HTTPServer(("127.0.0.0", 80), http.server.CGIHTTPRequestHandler)
s.serve_forever()
