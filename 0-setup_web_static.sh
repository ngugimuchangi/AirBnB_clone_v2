#!/usr/bin/env bash
# Script that  install nginx an configure it to serve static website

pattern="server_name _;"
new_location="server_name _;\n\n\
	location /hbnb_static {\n\
		# hbnb web_static\n\
                alias /data/web_static/current;\n\
		index index.html;\n\
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
echo  -e "$html" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R  ubuntu:ubuntu /data/

# configure nginx and restart
sudo sed -i s@"$pattern"@"$new_location"@g temp
service nginx restart
