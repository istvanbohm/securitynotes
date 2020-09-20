
# RDP Client to Connect Windows Desktop

`rdesktop -g 1440x900 -k hu -u username -p password 10.10.10.1`

# File Transfer 

## SMB Server

### Start the SMB server

`impacket-smbserver shareName /home/kali/foo/bar/`

### Check the server status

`smbclient -L 10.10.10.1 --no-pass`

In case of "NT_STATUS_NOT_SUPPORTED" error, add the following lines to the [GLOBAL] section of the "/etc/samba/smb.conf" file:

```
client min protocol = CORE
client max protocol = SMB3
```

### Access to the share from Windows

`\\10.10.10.1\shareName\foobar.exe`
