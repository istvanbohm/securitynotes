
# Checking SSL Certificate

`openssl s_client -connect target.com:443 -showcerts`


# Viewing SSL Certificate Details

```
cat target.com_443.crt | openssl x509 -text -noout
openssl s_client -connect target.com:443 -showcerts
```

