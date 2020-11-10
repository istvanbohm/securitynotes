
# RDP Client to Connect Windows Desktop

`rdesktop -g 1440x900 -k hu -u username -p password 10.10.10.1`

# File Transfer 

## SMB Server

### Start the SMB server

`sudo impacket-smbserver shareName /home/kali/foo/bar/`

### Check the server status

`smbclient -L 10.10.10.1 --no-pass`

In case of "NT_STATUS_NOT_SUPPORTED" error, add the following lines to the [GLOBAL] section of the "/etc/samba/smb.conf" file:

```
client min protocol = CORE
client max protocol = SMB3
```

### Access to the share from Windows

`\\10.10.10.1\shareName\foobar.exe`

## Rsync
`rsync -azP john@10.10.10.1:/home/john/tools ./`

## SCP

`scp -r user01@10.10.10.1:~/foo/bar/ .`

`scp user01@10.10.10.1:~/foo/bar/foobar .`

## Download multiple files listed in a text file

`wget --no-check-certificate -q -i urllist.txt`

## Mount remote directory

`sshfs john@10.10.10.1:/remote/directory /local/mount/point`

`mount -t cifs -o user=john //10.10.10.1/myshare /local/mount/point`


# Listen Incomming SMTP Connections

`sudo python3 -m smtpd -n -c DebuggingServer 0.0.0.0:25`

# Simple HTTP Server

`python3 -m http.server 8080`
`python -m SimpleHTTPServer 8080`

# MISC

## Useful commands
`ps -aef --forest`

## Disable Beep/Bell

remove the beep/bell module

`sudo modprobe -r pcspkr`

## Configure System Proxy Settings

```
export http_proxy=http://username:password@127.0.0.1:8080
export https_proxy=https://username:password@127.0.0.1:8080
```

## Beautify Code

### JavaScript

```
pip install jsbeautifier
js-beautify app.js > beautified_app.js
```
