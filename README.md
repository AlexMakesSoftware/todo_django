# README.md

Test app for my CI/CD project (Pull N Pray). This was based on a training/presentation I gave at work called 'a quick intro to Django', which I've included in this project.

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


## Environmental config
You should generate a secret key and put it in a file in the root of the project called '.env', like so:
SECRET_KEY = '<your key value here>'

There are various ways to generate this value, I suggest:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set this to whatever your domain name is:
MY_HOST = "my-app.example.com"

I suggest this for the static assets folder, but you can use whatever you like:
STATIC_ASSETS_FOLDER = "var/www/static/"

Don't source control '.env'! - this is are your environment-specific (and secret) settings.


## Running

Once you've installed this app locally and set up your reverse proxy to it, you should be able to access it with:

```
./run_prod.sh
```
Of course, you can install it as a service, or just run it in the background - it's up to you.
