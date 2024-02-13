import string
import random

random_str = string.ascii_lowercase + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@host.docker.internal/flask-test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key