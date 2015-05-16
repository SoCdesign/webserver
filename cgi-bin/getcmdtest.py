#!/usr/bin/python
import cgitb; cgitb.enable()

# The subprocess module is new in 2.4
import os, urllib, subprocess as sub

# Retrieve the command from the query string
# and unencode the escaped %xx chars
str_command = urllib.unquote(os.environ['QUERY_STRING'])
#str_command = "nc localhost 5555=eren c :)"
if str_command = "1":
	commands = '''
	echo 1 2 3 4 5
	'''

if str_command = "2":
	commands = '''
	echo 1 2 3 4 5
	'''

if str_command = "3":
	commands = '''
	echo 1 2 3 4 5
	'''

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