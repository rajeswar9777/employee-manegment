import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Basic Flask settings
    DEBUG = True

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'employees.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management
    SECRET_KEY = 'your_secret_key_here'
