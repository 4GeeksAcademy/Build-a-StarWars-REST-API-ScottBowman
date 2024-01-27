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



@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@api.route('/users/', methods=['POST'])
def create_user():
    request_body = request.get_json()
    user = User(username=request_body["username"], password=request_body["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 200

@api.route('/users/<int:id>', methods=['GET'])
def get_single_user(id):
    user = User.query.get(id)
    return jsonify(user.to_dict()), 200

@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.to_dict(),'deleted'), 200




@api.route('/planets/<int:id>', methods=['GET'])
def get_single_planet(id):
    planet = Planet.query.get(id)
    return jsonify(planet.to_dict()), 200

@api.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([planet.to_dict() for planet in planets]), 200

@api.route('/planets', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    planet = Planet(name=request_body["name"], climate=request_body["climate"], terrain=request_body["terrain"], population=request_body["population"])
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.to_dict()), 200

@api.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)
    db.session.delete(planet)
    db.session.commit()
    return jsonify(planet.to_dict(),'deleted'), 200

# Character Routes
@api.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return jsonify([character.to_dict() for character in characters]), 200

@api.route('/character', methods=['POST'])
def create_character():
    request_body = request.get_json()
    character =  Character(name=request_body["name"], height=request_body['height'], hair_color=request_body['hair_color'], eye_color=request_body['eye_color'], gender=request_body['gender'])
    db.session.add(character)
    db.session.commit()
    return jsonify(character.to_dict()), 200

@api.route('/character/<int:character_id>', methods=['GET'])
def get_single_character(character_id):
    character = Character.query.get(character_id)
    return jsonify(character.to_dict()), 200

@api.route('/character/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = Character.query.get(character_id)
    db.session.delete(character)
    db.session.commit()
    return jsonify(character.to_dict(),'deleted'), 200

# Favorite Routes
@api.route('/favorites', methods=['GET'])
def get_favorites():
    favorites = Favorite.query.all()
    return jsonify([favorite.to_dict() for favorite in favorites]), 200

@api.route('/favorite', methods=['POST'])
def create_favorite():
    request_body = request.get_json()
    favorite = Favorite(user_id=request_body["user_id"], planet_id=request_body["planet_id"], character_id=request_body["character_id"])
    db.session.add(favorite)
    db.session.commit()
    return jsonify(favorite.to_dict()), 200

@api.route('/favorite/<int:favorite_id>', methods=['GET'])
def get_single_favorite(favorite_id):
    favorite = Favorite.query.get(favorite_id)
    return jsonify(favorite.to_dict()), 200

@api.route('/favorite/<int:favorite_id>', methods=['DELETE'])
def delete_favorite(favorite_id):
    favorite = Favorite.query.get(favorite_id)
    db.session.delete(favorite)
    db.session.commit()
    return jsonify(favorite.to_dict(),'deleted'), 200

