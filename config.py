import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv

# set up user oauth
# http://bitwiser.in/2015/09/09/add-google-login-in-flask.html

basedir = abspath(dirname(__file__)) + '/.env'
load_dotenv(basedir)

class Auth:
  CLIENT_ID = os.environ.get('client_id')
  CLIENT_SECRET = os.environ.get('client_secret')
  REDIRECT_URI = 'http://127.0.0.1:5000/'
  AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
  TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
  USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'

class Config:
  APP_NAME = "Test Google Login"
  SECRET_KEY = os.environ.get("SECRET_KEY") or "somethingsecret"


class DevConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")


class ProdConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")


config = {
  "dev": DevConfig,
  "prod": ProdConfig,
  "default": DevConfig
}

__file__ = '.env'
