from os import path, environ

basedir = path.abspath(path.dirname(path.dirname(__file__)))

class Config:
    DEBUG = False
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTGRES_ADDR = environ.get('POSTGRES_ADDR')
    POSTGRES_USER = environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_ADDR}:5432/inventory_development"


class TestingConfig(Config):
   pass


class ProductionConfig(Config):
    pass

config = {
    "docker": DevelopmentConfig,
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig
}

# key = Config.SECRET_KEY