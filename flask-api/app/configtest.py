from random import choice
import string

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = '.'.join(choice(random_str) for i in range(12))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@host.docker.internal/flask-test'
TESTING = True,
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key