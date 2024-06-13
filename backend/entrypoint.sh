#!/bin/bash

if [ -d /sveltedjango/media/public ]; then
    rm -rf /sveltedjango/media/public
fi

mkdir -p /sveltedjango/media/public
cp -r /sveltedjango/public/* /sveltedjango/media/public/

python3 manage.py migrate
gunicorn $PROJECT_NAME.wsgi:application --bind 0.0.0.0:8000

exec "$@"