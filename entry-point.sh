#!/usr/bin/env bash

pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --no-input
mkdir logs
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log
tail -n 0 -f ./logs/gunicorn*.log &

gunicorn --bind :8000 personal_finance_manager.wsgi:application --reload
--log-level=info --log-file=./logs/gunicorn.log --access-logfile=
./logs/gunicorn-access.log --name=finance-manager

exec "$@"