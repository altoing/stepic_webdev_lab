sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

mkdir -p /home/box/web/public/{img,css,js}                                      
mkdir -p /home/box/web/{uploads,etc}
mkdir /etc/gunicorn.d/

ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
