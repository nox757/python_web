#sudo ln -sf /usr/bin/python3 /usr/bin/python

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
#cd /home/box/web
sudo /home/box/web/gunicorn -c /etc/gunicorn.d/hello.py hello:wsgi_application
