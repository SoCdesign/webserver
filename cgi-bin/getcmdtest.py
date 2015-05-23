#!/usr/bin/python
import cgitb; cgitb.enable()

# The subprocess module is new in 2.4
import os, urllib, subprocess as sub

# Retrieve the command from the query string
# and unencode the escaped %xx chars
str_command = urllib.unquote(os.environ['QUERY_STRING'])
#str_command = "nc localhost 5555=eren c :)"

#100Hz
if str_command = "1":
    slv_reg0 = "00_00_0000_0000_0000_1011_0010_0000_0101"
    slv_reg1 = "00_00_0000_0000_0001_0110_0100_0000_1010"
    slv_reg2 = "00_00_0000_0000_0000_1011_0010_0000_0101"
    slv_reg3 = "10_00_0001_0010_1111_0100_1010_1101_0010"
    slv_reg4 = "00_11_1110_1101_0011_0111_1101_0100_0011"

#1kHz
if str_command = "2":
    slv_reg0 = "00_00_0000_0100_0000_0010_1001_0110_1101"
    slv_reg1 = "00_00_0000_1000_0000_0101_0010_1101_1010"
    slv_reg2 = "00_00_0000_0100_0000_0010_1001_0110_1101"
    slv_reg3 = "10_00_1011_1101_0001_0111_0011_1010_0011"
    slv_reg4 = "00_11_0101_0010_1111_0011_0010_0001_0001"

#10kHz
if str_command = "3":
    slv_reg0 = "00_00_1110_0001_0111_1010_1011_1000_0011"
    slv_reg1 = "00_01_1100_0010_1111_0101_0111_0000_0110"
    slv_reg2 = "00_00_1110_0001_0111_1010_1011_1000_0011"
    slv_reg3 = "11_10_1100_0101_0000_1101_0101_0011_0000"
    slv_reg4 = "00_00_1100_0000_1101_1101_1000_1101_1101"

commands = '''
echo %s %s %s %s %s
''' % (slv_reg0, slv_reg1, slv_reg2, slv_reg3, slv_reg4)

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