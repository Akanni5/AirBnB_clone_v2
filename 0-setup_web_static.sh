#!/usr/bin/env bash
# bash script that sets up a web server for
# deployment.

# install nginx

apt-get -y update
apt-get -y install nginx

# create the necessary folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# test html file
echo "Hello web_static" > /data/web_static/releases/test/index.html
# create a symlink
ln -s -f /data/web_static/releases/test /data/web_static/current
# give ownership of the ubuntu user and group.
chown -h -R ubuntu:ubuntu /data/

# backup the configuration file
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.original

# nginx configuration to serve the content of /data/web_static/current/
sudo sed -i '/^server {/,/^}/s/^}/\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n}/' /etc/nginx/sites-available/default

service nginx restart
