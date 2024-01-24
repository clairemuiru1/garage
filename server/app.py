#!/usr/bin/env python3

import os
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from models import db, Garage ,Service , SparePart

app = Flask(__name__)
# CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class Signup(Resource):
    pass

class CheckSession(Resource):
    pass

class Login(Resource):
    pass

class Logout(Resource):
    pass

class GarageResource(Resource):
    pass

class GarageByID(Resource):
    pass

class ServiceResource(Resource):
    pass

class SparePartResource(Resource):
    pass

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(GarageResource, '/garage')
api.add_resource(GarageByID, '/garage/<int:id>')
api.add_resource(ServiceResource, '/service')
api.add_resource(SparePartResource, '/sparepart')


if __name__ == '__main__':
    app.run(port=5555, debug=True)