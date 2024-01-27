"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User,Planet, Character, Favorite
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

api = Blueprint('api', __name__)

# User Routes
@api_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@api_blueprint.route('/user', methods=['POST'])
def create_user():
    data = request.get.json
    

@api_blueprint.route('/users/<int:id>', methods=['GET'])

@api_blueprint.route('/users/<int:id>', methods=['PUT'])

@api_blueprint.route('/users/<int:id>', methods=['DELETE'])

# Planet Routes
@api_blueprint.route('/planets', methods=['GET'])

@api_blueprint.route('/planet', methods=['POST'])

@api_blueprint.route('/planets/<int:id>', methods=['GET'])

@api_blueprint.route('/planets/<int:id>', methods=['PUT'])

@api_blueprint.route('/planets/<int:id>', methods=['DELETE'])

# Character Routes
@api_blueprint.route('/characters', methods=['GET'])

@api_blueprint.route('/character', methods=['POST'])

@api_blueprint.route('/character/<int:character_id>', methods=['PUT'])

@api_blueprint.route('/character/<int:character_id>', methods=['DELETE'])

# Favorite Routes
@api_blueprint.route('/favorites', methods=['GET'])

@api_blueprint.route('/favorite', methods=['POST'])

@api_blueprint.route('/favorite/<int:favorite_id>', methods=['PUT'])

@api_blueprint.route('/favorite/<int:favorite_id>', methods=['DELETE'])




    return jsonify(response_body), 200
