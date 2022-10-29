#!/usr/bin/env bash
# Script that  install nginx an configure it to serve static website

new_location="\tlocation /hbnb_static {\n\
		# hbnb web_static\n\
        alias /data/web_static/current;\n\
		index index.html;\n\
	}\n"

# install nginx
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx

# create web static directories and files
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo  -e "It is the way" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R  ubuntu:ubuntu /data/

# configure nginx and restart
sudo sed -i "38i\\$new_location" /etc/nginx/sites-available/default
service nginx restart
