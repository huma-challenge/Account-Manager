# Sync dev settigns wtih base settings
from config.settings.base import *

import environ
import os

# Define and loads env var files
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR / "config/django.dev.env"))
environ.Env.read_env(os.path.join(BASE_DIR / "config/postgresql.dev.env"))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

# Create A list of hosts from env var
ALLOWED_HOSTS = str(env("ALLOWED_HOSTS")).strip('"').strip().split()

INSTALLED_APPS += [
    "django_grpc_framework",
    "account_manager.account",
    "account_manager.api",
    "account_manager.auth_system",
]

ROOT_URLCONF = "config.urls.dev"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}
