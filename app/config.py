from os import environ

class Config(object):
    SECRET_KEY = environ['SESSION_SECRET']
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 8080
    
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = environ['SECURITY_PASSWORD_SALT']
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True
    
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_SSL = False
    
    CELERY_RESULT_BACKEND = 'redis://localhost'
    CELERY_ENABLE_UTC = True
    BROKER_URL = 'redis://localhost'
    
    ASSETS_DEBUG = True

class ProductionConfig(Config):
    ASSETS_DEBUG = False
    MAIL_USE_SSL = True
    DEBUG = False

class DevelopmentConfig(Config):
    MAIL_PORT = 2048
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class TestingConfig(Config):
    TESTING = True