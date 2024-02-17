from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from app.models import User
from app.routes.utils import check_login, hash_password
from bson import ObjectId
from bcrypt import gensalt

users_bp = Blueprint('users', __name__)

@users_bp.route("/login",  methods=["POST"])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = User.collection.find_one({'username': username}, {'password': 1, 'salt': 1, 'rol': 1, '_id': 1})
    print('userrr: ', user)
    if user and check_login(user, password):
        access_token = create_access_token(identity={'user_id': str(user.get('_id')), 'rol': user.get('rol')})
        return jsonify({'access_token': access_token, 'rol': user.get('rol') }), 200
    else:
        return jsonify({'message': 'Usuario o contraseñas inválidas'}), 401

@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")

    existing_user = User.collection.find_one({"username": username})
    
    if existing_user:
        return jsonify({"error": "El usuario ya existe"}), 400
    
    salt = gensalt()
    data['password'] = hash_password(data['password'], salt)
    data['salt'] = salt
    insert_result = User.collection.insert_one(data)
    new_user_id = insert_result.inserted_id
    
    return jsonify({'message': 'Usuario creado exitosamente', 'user_id': str(new_user_id)})

@users_bp.route("/users", methods=["GET"])
def get_users():
    users = User.collection.find({}, {'salt': 0})
    users_list = list(users)
    for user in users_list:
        user['_id'] = str(user['_id'])
        
    return jsonify({"users": users_list}), 200

@users_bp.route("/users/<string:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.collection.find_one({'_id': ObjectId(user_id)}, {'password': 0, 'salt': 0})
    user['_id'] = str(user['_id'])
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
@users_bp.route("/users/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    salt = gensalt()
    if 'password' in data:
        data['password'] = hash_password(data['password'], salt)
        data['salt'] = salt
    result = User.collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
    if result.modified_count == 1:
        return jsonify({'message': 'Usuario actualizado exitosamente'})
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

@users_bp.route("/users/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = User.collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'Usuario eliminado exitosamente'})
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
