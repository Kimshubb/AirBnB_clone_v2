#!/usr/bin/env bash
# Installs Nginx if it not already installed
# Creates a fake HTML file /data/web_static/releases/test/index.html
# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder

# install ngnix
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# create index.html recursively
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/i
echo "Hello World! From Shawn" > /data/web_static/releases/test/index.html

# linking files
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# making ubuntu owner of files
sudo chown -hR ubuntu:ubuntu /data

# Add server config
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
