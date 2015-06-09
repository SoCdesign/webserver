#!/usr/bin/python
import cgitb; cgitb.enable()
import os, urllib, subprocess as sub
from coff import *

# Retrieve the command from the query string
# and unencode the escaped %xx chars
str_command = urllib.unquote(os.environ['QUERY_STRING'])
coeff = []

if str_command.split("=")[0] == "low":
    b, a = lowpass(str_command.split("=")[1])
    coeff.append("00" + convert(b[0]))
    coeff.append("01" + convert(b[1]))
    coeff.append("02" + convert(b[2]))
    coeff.append("03" + convert(a[1]))
    coeff.append("04" + convert(a[2]))
    
#elif str_command.split("=")[0] == "band":
#    a = lowpass(str_command.split("=")[1])
#    strcmd = "echo 01AABBCCDD > /proc/superip"

elif str_command.split("=")[0] == "high":
    b, a = highpass(str_command.split("=")[1])
    coeff.append("10" + convert(b[0]))
    coeff.append("11" + convert(b[1]))
    coeff.append("12" + convert(b[2]))
    coeff.append("13" + convert(a[1]))
    coeff.append("14" + convert(a[2]))


for x in coeff:
    strcmd = "echo " + x + " > /proc/superip"
    p = sub.Popen(['/bin/bash', '-c', strcmd], 
        stdout=sub.PIPE, stderr=sub.STDOUT)
    output = urllib.unquote(p.stdout.read())




print """\
Content-Type: text/html\n
<html><body>
<pre>
$ %s
%s
</pre>
</body></html>
""" % (strcmd, output)
