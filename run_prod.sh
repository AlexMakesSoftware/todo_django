#!/bin/bash
gunicorn -c conf/gunicorn_config.py todo.wsgi:application
