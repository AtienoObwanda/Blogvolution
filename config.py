import os

class Config:
    '''
    Parent config class
    '''

    SECRET_KEY =os.environ.get('SECRET_KEY')
    #lite:
    # SQLAlCHEMY_DATABASE_URI = 'sqlite://site.db'
    # For migrations
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://atieno:mishi@localhost/blog'
    # for prod
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #.replace("://", "ql://", 1)
    # SQLALCHEMY_TRACK_MODIFICATIONS= False

class ProdConfig(Config):
    '''
    ProdConfig --> child class
    '''
    pass

class DevConfig(Config):
    '''
    DevConfig --> child class
    '''
    # SQLAlCHEMY_DATABASE_URI = 'sqlite://site.db'

    # For migrations
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://atieno:mishi@localhost/blog' 
    
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}