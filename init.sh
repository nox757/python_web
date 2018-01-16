#sudo ln -sf /usr/bin/python3 /usr/bin/python

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


#cd /home/box/web
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:wsgi_application
gunicorn -b 0.0.0.0:8000 ask.wsgi:application&    

#####sudo /etc/init.d/mysql start
# CREATE DATABASE stepic CHARACTER SET UTF8;
# CREATE USER box IDENTIFIED BY '';
# GRANT ALL PRIVILEGES ON stepic.* TO box;
# FLUSH PRIVILEGES;