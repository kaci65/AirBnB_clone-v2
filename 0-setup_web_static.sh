#!/usr/bin/env bash
# Bash script that sets up web servers for deployment of web_static

#insttall nginx if not already installed
if ! which nginx > /dev/null 2>&1; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo ufw allow 'Nginx HTTP'
    sudo service nginx start
fi

# create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create fake html file
echo "
<!DOCTYPE html>
<html>
  <head>
	<title>Fake File</title>
  </head>
  <body>
    <p>Hello World!</p>
  </body>
</html>" > /data/web_static/releases/test/index.html

# create a symbolic link (symlink)
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change both the owner and group owner at the same time
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
# serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server;/location/hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# restart nginx & exit successfully
sudo service nginx restart
exit 0
