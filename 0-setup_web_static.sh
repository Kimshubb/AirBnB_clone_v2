#!/usr/bin/env bash
#set up server for deployment of web static
if command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <h1>This is a test page</h1>
    <p>Hello, world!</p>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R www-data:www-data /data/
sudo sed -i '/server {/a \ \ \ \ location /hbnb_static/ { alias /data/web_static/current/; } }' /etc/nginx/sites-available/default

sudo service nginx restart
exit 0
