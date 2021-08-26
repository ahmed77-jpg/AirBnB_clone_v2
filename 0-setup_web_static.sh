#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo echo "Hey AIrbnb" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
sudo service nginx start
sudo service nginx restart
