import os
from os import environ

class Config(object):
    
    Debug = False
    TESTING = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    SECRET_KEY = 'pianalytix'
    
    UPLOADS = "/home/username/app/app/static/uploads"
    
    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None
    
class DevelopmentConfig(Config):
    
    Debug = True
    SEESION_COOKIE_SECURE = False
   
class DebugConfig(Config):
    
    Debug = False 
   