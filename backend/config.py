import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'jnj324jn#<>GWE43434t'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql + pymysql: // <db_user >: < db_password >@< endpoint > / < db_url >'

    # Your secret key goes here
    SECRET_KEY = 'p9Bv<3Eid9%$i01'


class TestingConfig(Config):
    TESTING = True