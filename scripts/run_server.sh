#!/usr/bin/env bash

cd NVD/
python manage.py migrate --no-input
gunicorn NVD.wsgi -b 0.0.0.0:8000 --reload