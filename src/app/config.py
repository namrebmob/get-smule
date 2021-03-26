# config.py

import os
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
