#!/usr/bin/python
import http.server
import os

s = http.HTTPServer(("0.0.0.0", os.environ.get("PORT")), http.server.CGIHTTPRequestHandler)
s.server_forever()
