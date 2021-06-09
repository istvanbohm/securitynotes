# Tools

## Bruteforce Files and Directories

`gobuster dir -k -w ./wordlist.txt -u https://10.10.10.1/foo/bar/ -c PHPSESSID=aaa`

`dirb https://10.10.10.1/foo/bar/ ./wordlist.txt -c PHPSESSID=aaa -r`

# Wordlists

## Kali

```
/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirb/big.txt
```

## SecLists

https://github.com/danielmiessler/SecLists

`sudo apt install seclists`

## FuzzDB 

https://github.com/fuzzdb-project/fuzzdb

## Generate the list of the top 10k most popular npm packages

```
wget https://github.com/nice-registry/all-the-package-names/raw/master/names.json
jq '.[0:10000]' names.json | grep ","| cut -d'"' -f 2 > npm-10000.txt
```
