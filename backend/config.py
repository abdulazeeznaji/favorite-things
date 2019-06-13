import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'jnj324jn#<>GWE43434t'


class ProductionConfig(Config):
    DEBUG = False

    # AWS
    FLASKS3_BUCKET_NAME = os.environ.get('FLASKS3_BUCKET_NAME')
    FLASKS3_URL_STYLE = os.environ.get('FLASKS3_URL_STYLE')
    FLASKS3_BUCKET_DOMAIN = os.environ.get('FLASKS3_BUCKET_DOMAIN')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    """
    Development configurations
    """
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dt_admin:dt2016@localhost/dreamteam'

    # Your secret key goes here
    SECRET_KEY = 'p9Bv<3Eid9%$i01'


class TestingConfig(Config):
    TESTING = True