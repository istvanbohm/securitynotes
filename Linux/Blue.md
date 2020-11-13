

## View Process Tree

ps -aef --forest

## Identify Backdoor Shells

ps -aef --forest
# look for the PID of /bin/bash
cd /proc/<<<PID>>>
ls -la | grep cwd

get attacker ip
# sh -c /bin/sh
ss -anp | grep <<<PID>>>

## Logs 

/var/log/apache2/access.log

