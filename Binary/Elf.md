# pwntools

## Install pwntools

http://docs.pwntools.com/en/stable/index.html

```
$ apt-get update
$ apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade pwntools
```

# What protections has the binary?

`$ checksec --file=vulnerable`

# Checking the binary function names

`$ readelf -a vulnerable | grep FUNC | grep -vi glibc`
