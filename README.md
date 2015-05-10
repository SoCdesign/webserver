# webserver
Readme!

ZEDBOARD (WEBSERVER):

you should start with install apache2

	"sudo apt-get install apache2"

then you should copy our original "www" folder to "var/www"

then add this lines below to "/etc/apache2/sites-available/000-def.conf"

	"""
    	ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"    
    	<Directory /var/www/cgi-bin>
        	Options +ExecCGI
        	AddHandler cgi-script .sh .py
        	Options FollowSymLinks
        	Require all granted
    	</Directory>

	"""

then time to give permission to scripts for execute them by apache

	"sudo chmod 755 /usr/lib/getcmd.py"
	"sudo chmod 755 /usr/lib/get2cmd.py"

then enabling cgi mod

	"sudo a2enmod cgi"

now you can restart server and its done!

	"sudo service apache2 restart"

Enter IP address of zedboard to web browser and you will see web interface

OTHER ZEDBOARDS:

	"""
	$mkfifo /tmp/tmp_fifo
	$cat /tmp/tmp_fifo | /bin/sh -i 2>&1 | nc -l 5555 > /tmp/tmp_fifo
	"""

this lines above should be added to startup configurations of zedboards
