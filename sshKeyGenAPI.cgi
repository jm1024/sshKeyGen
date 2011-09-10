#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>sshKeyGenRaw</title></head><body>"
rm /tmp/keyTemp | /dev/null
rm /tmp/keyTemp.pub  | /dev/null
ssh-keygen -t rsa -C "ssh@localhost" -f /tmp/keyTemp -P '' -q
cat /tmp/keyTemp.pub
echo "*********"
cat /tmp/keyTemp
cat "</body></html>"
