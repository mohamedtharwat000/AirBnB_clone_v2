#!/usr/bin/env bash
# Prepare a web server

sudo apt update
sudo apt upgrade -y
sudo apt install -y nginx

sudo service nginx start
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
printf \
"<html>
  <head>
  </head>
  <body>
    <h1>Test Nginx</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/server_name _;/a \ \n\tlocation /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default

sudo nginx -s reload
