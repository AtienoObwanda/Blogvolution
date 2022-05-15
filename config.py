import os

class Config:
    pass


class ProdConfig(Config):
    '''
    ProdConfig --> child class
    '''
    pass

class DevConfig(Config):
    '''
    DevConfig --> child class
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}