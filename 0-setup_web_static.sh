#!/usr/bin/env bash
# Scrip that  install nginx an configure it to serve static website
pattern="server_name localhost;"
new_location="server_name localhost;\n\n\
	location /hbnb_static {\n\
		# hbnb web_static\n\
                alias /data/web_static/current;\n\
	}\n\n"
# install nginx if not install
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx

# create web static directories and files
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown -R  ubuntu:ubuntu /data
echo "Welcome to HBNB" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current

# configure nginx and restart
sudo sed -i s@"$pattern"@"$new_location"@g /etc/nginx/sites-available/default
sudo nginx -s reload
