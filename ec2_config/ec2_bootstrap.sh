#!/bin/bash

echo "#######################################"  >> /var/log/riverwavestat_log
echo "######## APT-GET UPDATE"                  >> /var/log/riverwavestat_log
echo "#######################################"  >> /var/log/riverwavestat_log
sudo apt-get update                             >> /var/log/riverwavestat_log

echo "#######################################"  >> /var/log/riverwavestat_log
echo "######## APT GET PYTHON + PIP"            >> /var/log/riverwavestat_log
echo "#######################################"  >> /var/log/riverwavestat_log
sudo apt-get install python3.8 -y               >> /var/log/riverwavestat_log
sudo apt-get install python3-pip -y             >> /var/log/riverwavestat_log

echo "#######################################"  >> /var/log/riverwavestat_log
echo "######## SYMLINKS PYTHON + PIP"           >> /var/log/riverwavestat_log
echo "#######################################"  >> /var/log/riverwavestat_log
sudo rm -rf /usr/bin/python                     >> /var/log/riverwavestat_log
sudo rm -rf /usr/bin/pip                        >> /var/log/riverwavestat_log
sudo ln -sT /usr/bin/python3 /usr/bin/python    >> /var/log/riverwavestat_log
sudo ln -sT /usr/bin/pip3 /usr/bin/pip          >> /var/log/riverwavestat_log

echo "#######################################"  >> /var/log/riverwavestat_log
echo "######## APT GET VIRTUALENV"              >> /var/log/riverwavestat_log
echo "#######################################"  >> /var/log/riverwavestat_log
sudo apt-get install virtualenv -y              >> /var/log/riverwavestat_log

echo "#######################################"  >> /var/log/riverwavestat_log
echo "######## APT GET APACHE2 + WSGI + LYNX"   >> /var/log/riverwavestat_log
echo "#######################################"  >> /var/log/riverwavestat_log
sudo apt-get install apache2 -y                 >> /var/log/riverwavestat_log
sudo apt-get install libapache2-mod-wsgi-py3 -y >> /var/log/riverwavestat_log
sudo apt-get install lynx -y                    >> /var/log/riverwavestat_log

echo "#######################################" >> /var/log/riverwavestat_log
echo "######## SYMLINK TO VAR/WWW/HTLM"        >> /var/log/riverwavestat_log
echo "#######################################" >> /var/log/riverwavestat_log
sudo ln -sT /home/ubuntu//RiverwaveStatWebsite /var/www/html/riverwavestat  >> /var/log/riverwavestat_log

echo "#######################################"  >> /var/log/riverwavestat_log
echo "######## CONFIG VENV + REQUIREMENTS"      >> /var/log/riverwavestat_log
echo "#######################################"  >> /var/log/riverwavestat_log
cd /home/ubuntu/RiverwaveStatWebsite            >> /var/log/riverwavestat_log
virtualenv riverwavestat                        >> /var/log/riverwavestat_log
source riverwavestat/bin/activate               >> /var/log/riverwavestat_log
pip install -r requirements.txt                 >> /var/log/riverwavestat_log

echo "#######################################" >> /var/log/riverwavestat_log
echo "######## CONFIG VENV + REQUIREMENTS"     >> /var/log/riverwavestat_log
echo "#######################################" >> /var/log/riverwavestat_log
sudo cp /home/ubuntu//RiveStatWebsite/ec2_config/apache_config.txt /etc/apache2/sites-enabled/000-default.conf   >> /var/log/riverwavestat_log

sudo apachectl restart                          >> /var/log/riverwavestat_log