from todo.base_settings import *

DEBUG = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
ALLOWED_HOSTS = [os.getenv("MY_HOST")]
CSRF_TRUSTED_ORIGINS = ["https://" + os.getenv("MY_HOST")]

# Database
# In reality, we wouldn't want to use sqlite in production, it'd be postgresql or something.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "prod_db.sqlite3",
    }
}
