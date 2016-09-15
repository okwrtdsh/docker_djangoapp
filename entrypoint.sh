#!/bin/sh
cd /code/src
export PYTHONPATH=/code/src
pip3 install -r /code/conf/package.pip
/usr/bin/python3 /code/src/manage.py collectstatic --settings=$DJANGO_SETTINGS_MODULE --noinput
/usr/bin/python3 /code/src/manage.py migrate --settings=$DJANGO_SETTINGS_MODULE --noinput
/usr/bin/uwsgi -M --ini /uwsgi.ini
