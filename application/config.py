import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'config.ini'))


class Config:
    SECRET_KEY = config.get('gallery', 'SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('gallery','SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = config.get('gallery', 'SQLALCHEMY_TRACK_MODIFICATIONS')
    MAIL_SERVER = config.get('gallery', 'MAIL_SERVER')
    MAIL_PORT = config.get('gallery', 'MAIL_PORT')
    MAIL_USE_TLS = config.get('gallery', 'MAIL_USE_TLS')
    MAIL_USERNAME = config.get('gallery', 'MAIL_USERNAME')
    MAIL_PASSWORD = config.get('gallery', 'MAIL_PASSWORD')
