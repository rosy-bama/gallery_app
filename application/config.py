import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'config.ini'))


class Config:
    SECRET_KEY = config.get('gallery', 'SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('gallery','SQLALCHEMY_DATABASE_URI')