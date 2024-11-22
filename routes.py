from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "E-mail já está registrado"}), 400

    new_user = User(
        email=email,
        password_hash=User.hash_password(password)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuário registrado com sucesso"}), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={"id": user.id, "email": user.email})
        return jsonify({"token": access_token}), 200

    return jsonify({"error": "Credenciais inválidas"}), 401

