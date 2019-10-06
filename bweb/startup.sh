#! /bin/sh

service ssh start
python3 /app/apsembb/manage.py runserver 0.0.0.0:80
