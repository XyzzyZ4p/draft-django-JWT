#!/bin/bash


BASE_PATH="$(dirname "$(dirname "$(readlink -fm "$0")")")"

if [ -z ${DEV_APP_SERVER_HOST+x} ]; then
  DEV_APP_SERVER_HOST='127.0.0.1'
fi

if [ -z ${DEV_APP_SERVER_PORT+x} ]; then
  DEV_APP_SERVER_PORT='8080'
fi

python3 "$BASE_PATH"/manage.py runserver "$DEV_APP_SERVER_HOST:$DEV_APP_SERVER_PORT"
