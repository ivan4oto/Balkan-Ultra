import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init api
api = Flask(__name__)
CORS(api)

# set configs
api.config.update(
    MAIL_SERVER='balkanultra.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='balkan@balkanultra.com',
    MAIL_PASSWORD=os.environ["MAIL_PASSWORD"]
)

# ENV
ENV = 'dev'

if ENV == 'dev':
    api.debug = True
    # Database
    api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/balkandb'
else:
    api.debug = False
    # Database
    api.config['SQLALCHEMY_DATABASE_URI'] = ''

api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(api)

# Init ma
ma = Marshmallow(api)
