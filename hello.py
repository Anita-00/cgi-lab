#!/usr/bin/env python3
import os, json
env = os.environ

# prints out all environment variables in Python

print("Content-Type: text/plain") # lets browser know to expect plain text
print()
print(os.environ)

# prints out all environment variables as JSON

print("Content-Type: application/json") # let browser know to expect json
print()
print(json.dumps(dict(os.environ), indent=2))

# print query paramter data in html

print("Content-Type: text/html") # let browser know to expect html
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# shows user's browser in HTML

print("Content-Type: text/html") # let browser know to expect html
print()
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")
