#!/bin/bash

pipenv run gunicorn --bind 0.0.0.0:8000 --workers 10 atccore.wsgi
