sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

mkdir -p /home/box/web/public/{img,css,js}                                      
mkdir -p /home/box/web/{uploads,etc}
mkdir /etc/gunicorn.d/

rn -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/mysql start﻿
mysql -u root -e "create databse ASK_PROJECT;"
/home/box/web/ask/manage.py syncdb
