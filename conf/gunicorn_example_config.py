# This is an example of the kind of configuration you need to add to the deployment server.
# You shouldn't really check in code like this, which is specific to the machine you're deploying on.
# (unless you standardise the deployment environemnt with docker but that can come later).
command = '~/venv/bin/gunicorn'
pythonpath = '~/dev/todo'
bind = '127.0.0.1:8000'
workers = 3
