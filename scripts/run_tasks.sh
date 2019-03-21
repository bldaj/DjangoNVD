#!/usr/bin/env bash

cd NVD/
celery -A NVD worker -B -l INFO