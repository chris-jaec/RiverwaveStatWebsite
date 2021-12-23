#!/bin/bash

echo "#######################################"  
echo "######## APT-GET UPDATE"                  
echo "#######################################"  
sudo apt-get update                             

echo "#######################################"  
echo "######## APT GET PYTHON + PIP"            
echo "#######################################"  
sudo apt-get install python3.8 -y               
sudo apt-get install python3-pip -y             

echo "#######################################"  
echo "######## SYMLINKS PYTHON + PIP"           
echo "#######################################"  
sudo rm -rf /usr/bin/python                     
sudo rm -rf /usr/bin/pip                        
sudo ln -sT /usr/bin/python3 /usr/bin/python    
sudo ln -sT /usr/bin/pip3 /usr/bin/pip          

echo "#######################################"  
echo "######## APT GET VIRTUALENV"              
echo "#######################################"  
sudo apt-get install virtualenv -y              

echo "#######################################"  
echo "######## APT GET APACHE2 + WSGI + LYNX"   
echo "#######################################"  
sudo apt-get install apache2 -y                 
sudo apt-get install libapache2-mod-wsgi-py3 -y 
sudo apt-get install lynx -y                    

echo "#######################################" 
echo "######## SYMLINK TO VAR/WWW/HTLM"        
echo "#######################################" 
sudo rm -rf /var/www/html/riverwavestat        
sudo ln -sT /home/ubuntu/RiverwaveStatWebsite /var/www/html/riverwavestat  

echo "#######################################"  
echo "######## CONFIG VENV + REQUIREMENTS"      
echo "#######################################"
sudo rm -rf /home/ubuntu/RiverwaveStatWebsite/venv-riverwavestat
cd /home/ubuntu/RiverwaveStatWebsite            
virtualenv venv-riverwavestat
source venv-riverwavestat/bin/activate
pip install -r requirements.txt                 

echo "#######################################" 
echo "######## CONFIG VENV + REQUIREMENTS"     
echo "#######################################" 
sudo rm -rf /etc/apache2/sites-enabled/000-default.conf   
sudo cp /home/ubuntu/RiverwaveStatWebsite/ec2_config/apache_config.txt /etc/apache2/sites-enabled/000-default.conf

sudo apachectl restart