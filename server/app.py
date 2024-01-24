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