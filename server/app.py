#!/usr/bin/env python3

import os
from flask import Flask, request, make_response, jsonify, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
# from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from sqlalchemy.exc import IntegrityError
from models import db, Garage ,Service , SparePart ,User
from flask_cors import CORS 
from  flask_restful import reqparse


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1254'

# db = SQLAlchemy(app)


migrate = Migrate(app, db)

db.init_app(app)
bcrypt = Bcrypt(app)
api = Api(app)
CORS(app)

class SignupForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    email = StringField('Email', [validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])

class Signup(Resource):
    def post(self):
        form = SignupForm(request.form)

        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            new_user = User(username=username, email=email, _password_hash=hashed_password)

            try:
                db.session.add(new_user)
                db.session.commit()
                return {'message': 'User created successfully'}, 201
            except IntegrityError:
                db.session.rollback()
                return {'message': 'Username or email already exists. Please choose a different one.'}, 400
        else:
            return {'error': form.errors}, 400


class CheckSession(Resource):
    def get(self):
        if 'user_id' in session:
            return {'message': 'Session is active'}
        else:
            return {'message': 'Session is not active'}, 401

#login
class Login(Resource): 
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            return {'message': 'Login successful'}, 200
        else:
            return {'message': 'Invalid username or password'}, 401

class Logout(Resource):
    def post(self):
        if 'user_id' in session:
            session.pop('user_id')
            return {'message': 'Logout successful'}, 200
        else:
            return {'message': 'No active session to logout from'}, 401

class GarageResource(Resource):
    def get(self):
        garages = []
        for garage in Garage.query.all():
            garage_dict = {
                "id": garage.id,
                "name" : garage.name,
                "location": garage.location,
                "contact_number": garage.contact_number,
            }
            garages.append(garage_dict)
        
        response = make_response(
            jsonify(garages),
            200
        )
        return response

class GarageByID(Resource):
    def get(self, id):
        garage = Garage.query.filter_by(id=id).first()

        if garage:
            garage_dict = {
                "id": garage.id,
                "name": garage.name,
                "location": garage.location,
                "contact_number": garage.contact_number,
                "services": []
            }

            for service in garage.services:
                service_dict = {
                    "id": service.id,
                    "name": service.name,
                    "description": service.description,
                    "price": service.price,
                    "spare_parts": []
                }

                for spare_part in service.spare_parts:
                    spare_part_dict = {
                        "id": spare_part.id,
                        "name": spare_part.name,
                        "description": spare_part.description,
                        "price": spare_part.price,
                        "image": spare_part.image
                    }

                    service_dict["spare_parts"].append(spare_part_dict)

                garage_dict["services"].append(service_dict)

            response = make_response(
                jsonify(garage_dict),
                200
            )
        else:
            response = make_response(
                jsonify({"error": "Garage not found"}),
                404
            )

        return response


class ServiceResource(Resource):
    def get(self):
        services = []

        for service in Service.query.all():
            service_dict = {
                "id": service.id,
                "name": service.name,
                "description": service.description,
                "price": service.price
            }
            services.append(service_dict)

        response = make_response(
            jsonify(services),
            200
        )

        return response


class SparePartResource(Resource):
    def get(self):
        spare_parts = []
        for spare_part in SparePart.query.all():
            spare_part_dict = {
                "id": spare_part.id,
                "name": spare_part.name,
                "description": spare_part.description,
                "price": spare_part.price,
                "image": spare_part.image,
            }
            spare_parts.append(spare_part_dict)

        response = make_response(
            jsonify(spare_parts),
            200
        )

        return response

class SparePartByID(Resource):
    def get(self, id=None):
        if id:
            # Get a specific spare part by ID
            spare_part = SparePart.query.get(id)

            if spare_part:
                spare_part_dict = {
                    "id": spare_part.id,
                    "name": spare_part.name,
                    "description": spare_part.description,
                    "price": spare_part.price,
                    "image": spare_part.image,
                }

                response = make_response(
                    jsonify(spare_part_dict),
                    200
                )
            else:
                response = make_response(
                    jsonify({"error": "Spare part not found"}),
                    404
                )
        else:
            # Get all spare parts
            spare_parts = []
            for spare_part in SparePart.query.all():
                spare_part_dict = {
                    "id": spare_part.id,
                    "name": spare_part.name,
                    "description": spare_part.description,
                    "price": spare_part.price,
                    "image": spare_part.image,
                }
                spare_parts.append(spare_part_dict)

            response = make_response(
                jsonify(spare_parts),
                200
            )

        return response
def patch(self, id):
        spare_part = SparePart.query.get(id)

        if spare_part:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, help='Name of the spare part')
            parser.add_argument('description', type=str, help='Description of the spare part')
            parser.add_argument('price', type=float, help='Price of the spare part')
            parser.add_argument('image', type=str, help='URL or path to the image of the spare part')

            args = parser.parse_args()

            # Update spare part attributes if provided in the patch request
            if args['name']:
                spare_part.name = args['name']
            if args['description']:
                spare_part.description = args['description']
            if args['price']:
                spare_part.price = args['price']
            if args['image']:
                spare_part.image = args['image']

            db.session.commit()
            return {'message': 'Spare part updated successfully'}, 200
        else:
            return {'message': 'Spare part not found'}, 404
def delete(self, id):
        spare_part = SparePart.query.get(id)

        if spare_part:
            db.session.delete(spare_part)
            db.session.commit()
            return {'message': 'Spare part deleted successfully'}, 200
        else:
            return {'message': 'Spare part not found'}, 404




api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(GarageResource, '/garage')
api.add_resource(GarageByID, '/garage/<int:id>')
api.add_resource(ServiceResource, '/service')
api.add_resource(SparePartResource, '/sparepart')
api.add_resource(SparePartByID ,'/sparepart/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)