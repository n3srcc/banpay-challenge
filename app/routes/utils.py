from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from bcrypt import hashpw

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            rol = current_user['rol']
            current_user_rol = rol
            if current_user_rol not in roles:
                return jsonify({"mensaje": "No tienes permiso para acceder a esta ruta"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

def check_login(user, password):
    stored_password = user.get('password')
    hashed_password = hashpw(password.encode('utf-8'), user.get('salt')).decode('utf-8')
    if hashed_password == stored_password:
        return True
    return False

def hash_password(password, salt):
    hashed_password = hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
