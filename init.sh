#!/usr/bin/env bash
#git clone https://github.com/altoing/stepic_webdev_lab /home/box/web && sudo /home/box/web/init.sh
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

mkdir -p /home/box/web/public/{img,css,js}                                      
mkdir -p /home/box/web/{uploads,etc}
mkdir /etc/gunicorn.d/

ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/mysql start
mysql -u root -e "create database ASK_PROJECT;"

/home/box/web/ask/manage.py syncdb
