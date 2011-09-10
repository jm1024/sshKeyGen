#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Demo</title></head><body>"
rm /tmp/keyTemp | /dev/null
rm /tmp/keyTemp.pub  | /dev/null
ssh-keygen -t rsa -C "ssh@localhost" -f /tmp/keyTemp -P '' -q
echo "<font face='helvetica' size='2'>"
echo "<b>PUBLIC KEY<pin nan/b><BR>"
echo "</font>"
echo "<font face='courier' size='2'>"
echo "<textarea rows='8' cols='65'>"
cat /tmp/keyTemp.pub
echo "</textarea>"
echo "<br><br>"
echo "<font face='helvetica' size='2'>"
echo "<b>PRIVATE KEY</b><BR>"
echo "</font>"
echo "<font face='courier' size='2'>"
echo "<textarea rows='28' cols='65'>"
cat /tmp/keyTemp
echo "</textarea>"
echo "<BR></body></html>"
