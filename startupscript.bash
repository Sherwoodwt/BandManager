#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install python-pip python-dev build-essential -y
sudo apt-get install libmysqlclient-dev -y

sudo pip install --upgrade virtualenv

cd /usr/local
sudo mkdir virtualenvs
sudo chown ubuntu:ubuntu virtualenvs
cd virtualenvs/
virtualenv --no-site-packages bandenv
cd bandenv/

source bin/activate
pip install gunicorn django MySQL-python

////Get your code here, from S3 not git

cd PROJECTNAME

cat > start_gunicorn.sh << EOF
#!/bin/bash
set -e
LOGDIR=/usr/local/virtualenvs/bandenv/bandsite
LOGFILE=\$LOGDIR/bandsite.log
ERRORFILE=\$LOGDIR/error.log
NUM_WORKERS=3
ADDRESS=127.0.0.1:8000
cd /usr/local/virtualenvs/bandenv/bandsite/
source ../bin/activate
test -d \$LOGDIR || mkdir -p \$LOGDIR
exec gunicorn bandsite.wsgi:application -w \$NUM_WORKERS --bind=\$ADDRESS \
--log-level=debug \
--log-file=\$LOGFILE 2>>\$LOGFILE 1>>\$ERRORFILE &
EOF

chmod +x start_gunicorn.sh
./start_gunicorn.sh

sudo apt-get install nginx -y

sudo su
sudo cat > /etc/nginx/sites-enabled/default << EOL
upstream app_server_djangoapp {
    server localhost:8000 fail_timeout=0; 
}

SERVER=wget -qO- http://instance-data/latest/meta-data/public-ipv4;

server {
    #EC2 instance security group must be configured to accept http connections over Port 80 
    listen 80;
    server_name \$SERVER;

    access_log  /var/log/nginx/guni-access.log;
    error_log  /var/log/nginx/guni-error.log info;

    keepalive_timeout 5;

    # path for static files
    root /home/username/webapps/guni/static;

    location / {
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header Host \$http_host;
        proxy_redirect off;

        if (!-f \$request_filename) {
            proxy_pass http://app_server_djangoapp;
            break;
        }
    }
}
EOL
exit

sudo service nginx start