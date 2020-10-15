
# Analyse Logs

## Find the last modified file in the directory

`dir | sort LastWriteTime | select -last 1`

## Read the tail of the log file

`Get-Content database.log -wait -tail 1`

## Apply additional filters

`Get-Content database.log -wait -tail 1 | Select-String -Pattern "select version"` 
