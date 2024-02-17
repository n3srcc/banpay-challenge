from flask_jwt_extended import jwt_required
from flask import Blueprint, jsonify
from app.models import User
from app.routes.utils import role_required
from app.services.consumer import request

BASE_URL = 'https://ghibliapi.vercel.app/'

service_bp = Blueprint('services', __name__)

@service_bp.route("/films", methods=["GET"])
@jwt_required()
@role_required("films", "admin")
def get_films():
    films_data, status_code = request(f"{BASE_URL}films")
    return jsonify(films_data), status_code

@service_bp.route("/people", methods=["GET"])
@jwt_required()
@role_required("people", "admin")
def get_people():
    people_data, status_code = request(f"{BASE_URL}people")
    return jsonify(people_data), status_code

@service_bp.route("/locations", methods=["GET"])
@jwt_required()
@role_required("locations", "admin")
def get_locations():
    locations_data, status_code = request(f"{BASE_URL}locations")
    return jsonify(locations_data), status_code

@service_bp.route("/species", methods=["GET"])
@jwt_required()
@role_required("species", "admin")
def get_species():
    species_data, status_code = request(f"{BASE_URL}species")
    return jsonify(species_data), status_code

@service_bp.route("/vehicles", methods=["GET"])
@jwt_required()
@role_required("vehicles", "admin")
def get_vehicles():
    vehicles_data, status_code = request(f"{BASE_URL}vehicles")
    return jsonify(vehicles_data), status_code
