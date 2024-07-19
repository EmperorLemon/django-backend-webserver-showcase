#!/usr/bin/env bash

echo -e "\n\033[1;33m====== Container Starting ======\033[0m"
echo -e "\033[1;36mRunning in a $DJANGO_ENV environment\033[0m\n"

sleep 5

python /app/manage.py migrate
python /app/manage.py collectstatic --no-input
exec python -m daphne -b 0.0.0.0 -p 8000 django_backend.asgi:application