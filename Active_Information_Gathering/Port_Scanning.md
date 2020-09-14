
# Port Scaning

## NMAP

Network exploration tool and security / port scanner

### Examples:

#### CTF
```
nmap -Pn -T4 --top-ports 3000 -sVC -A -oN nmap.txt 10.10.10.1
nmap -Pn -T4 -p- -sVC -A -oN nmap.txt 10.10.10.1
nmap -Pn -T4 -sU -sVC -A -oN nmap.txt 10.10.10.1
```
#### Work
```
nmap -Pn --reason -v -sV -p- -oA target_name 10.10.10.1
nmap -Pn --reason -v -sV -p- -T2 -oA target_name 10.10.10.1
nmap -Pn --reason -v -sV -p- -oA target_name -iL scope.txt
```
#### Network
```
nmap -sn -oG host_sweep.txt 10.10.10.0/24 ; grep open host_sweep.txt | cut -d " " -f2 | grep -v Nmap > hosts.txt
nmap -p 80 -oG web_sweep.txt 10.10.10.0/24 ; grep open web_sweep.txt | cut -d " " -f2 | grep -v Nmap > web.txt
```

#### Scripts
```
nmap --script=dns-zone-transfer -p 53 ns2.targetnw.com
nmap --script=smtp-enum-users.nse --script-args userdb=path/to/username.lst  -p 25 10.11.1.5
nmap -v -p 139, 445 --script=smb-vuln-ms17-010 10.11.1.227
```

### Scan types:
```
-sS (TCP SYN scan) (# Prefered)
-sT (TCP connect scan)
-sU (UDP scan)
-sV (Enable Version scaning) - Probe open ports to determine service/version info
-sC (Enable Script scaning) - Performs a script scan using the default set of scripts.
-O (Enable OS detection)

-sn: No port scan (only host discovery)
-Pn: Treat all hosts as online (skip host discovery)
--osscan-guess: Guess if no perfect OS match
```

### Target ports:
```
-p-: Scan ports from 1 through 65535
-p 22,53,110,143,4564: Scan specified TCP ports 
-p U:53,111,137,T:21-25,80,139,8080: Scan specified ports 
--top-ports n: Scan the top n ports (# top 2000 for UDP is usually enough)
```

### Input/output:
```
-iL <inputfilename>: Input from list of hosts/networks
-oA <filename>: Output in normal format
-oA <basename>: Output in the three major formats at once
-oG <filename>: Grepable output
```

### Other options:
```
-T<0-5>: Set timing template (higher is faster)
--reason: Display the reason a port is in a particular state
-vvv: Full verbosity
--packet-trace
```
