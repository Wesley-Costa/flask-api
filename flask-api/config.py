import string
import random

random_str = string.ascii_lowercase + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:wc060400@localhost:3306/flaskapi'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key