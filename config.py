import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gabrielcoder:dushanbe2015@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY ='12345'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")




    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER=os.environ.get('MAIL_SERVER')
    MAIL_PORT=os.environ.get('MAIL_PORT')
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    sender = os.environ.get('MAIL_USERNAME')





class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  

class DevConfig(Config):
    
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings

    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gabrielcoder:dushanbe2015@localhost/carblog'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'gabrielcoder247@gmail.com'
    MAIL_PASSWORD = 'dushanbe2015'
    SUBJECT_PREFIX = 'pitchit'
    SENDER_EMAIL = 'gabrielcoder247@gmail.com'
    sender='gabrielcoder247@gmail.com'


    

    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig
}


