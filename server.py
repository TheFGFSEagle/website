#!/usr/bin/python
import http.server
import os

s = http.server.HTTPServer(("0.0.0.0", int(os.environ.get("PORT"))), http.server.CGIHTTPRequestHandler)
s.cgi_directories = ["/"]
s.serve_forever()
