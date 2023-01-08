
from os import getenv


"""
The database credentials
should be created at a .env file and pass here.
"""

class Config(object):
    

    #create a secret key and stored here.
    SECRET_KEY = getenv("SECRET_KEY")

        
  