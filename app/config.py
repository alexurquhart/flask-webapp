from os import environ

class Config(object):
    SECRET_KEY = environ['SESSION_SECRET']
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URI']
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 8080
    
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = '54db4f012a2d41124951b8517393f505'
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True
    
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_SSL = False

class ProductionConfig(Config):
    MAIL_USE_SSL = True
    DEBUG = False

class DevelopmentConfig(Config):
    MAIL_PORT = 2048
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG = True

class TestingConfig(Config):
    TESTING = True