#!/usr/bin/env bash
# Scrip that  install nginx an configure it to serve static website

# pattern="server_name ;"
new_location="server {\n\
	listen 80 default_server;\n\
	listen [::]:80 default_server;\n\
	root /var/www/html;\n\
	index index.html index.htm;\n\n\
	server_name localhost;\n\n\
	location /hbnb_static {\n\
		# hbnb web_static\n\
                alias /data/web_static/current;\n\
		index index.html\n\
	}\n\
}\n"
html="<html>\n\
  <head>\n\
  </head>\n\
  <body>\n\
    Holberton School\n\
   </body>\n\
</html>"

# install nginx
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx

# create web static directories and files
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown -R  ubuntu:ubuntu /data
echo  -e "$html" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current

# configure nginx and restart
# sudo sed -i s@"$pattern"@"$new_location"@g /etc/nginx/sites-available/default
echo -e "$new_location" | sudo tee etc/nginx/sites-available/default
service nginx restart
