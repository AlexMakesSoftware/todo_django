# README.md

Test app for my CI/CD project (Pull N Pray).

## First time setup
Before you begin, create a python virtual environment.

```
python3.11 -m venv venv
```
Keep your environments seperate for each application.

Activate the venv

```
source venv/bin/activate
```

Install the necessary packages with
```
pip install -r requirements.txt
```

You need to configure gunicorn, by making a file called gunicorn_config.py in the config directory (an example file is provided in that directory).

Command needs to point to where gunicorn is installed.

command = '~/venv/bin/gunicorn'

Python Path needs to point to your django project.

pythonpath = '~/dev/todo'

## Running

Once you've installed this app locally and set up your reverse proxy to it, you should be able to access it with:

```
./run_prod.sh
```
Of course, you can install it as a service, or just run it in the background - it's up to you.

*Test.*
