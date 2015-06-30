killall -9 dhclient
dhclient eth0
sudo apt-get -y install apache2
sudo apt-get -y install python-scipy
sudo apt-get -y install libapache2-mod-python
sudo cp -r /mnt/web/www/ /var/
sudo cp /mnt/web/000-default.conf /etc/apache2/sites-available/
sudo cp /mnt/web/apache2.conf /etc/apache2/
sudo service apache2 restart