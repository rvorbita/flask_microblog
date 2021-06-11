import os

baseDIR=os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Define Config SECRET KEY"""
    SECRET_KEY =  os.environ.get('SECRET_KEY') or 'wonderful-day'
    """ SQL ALCHEMY CONFIG"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(baseDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False