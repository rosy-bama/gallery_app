from flask import Blueprint, request, jsonify
import uuid, secrets
from application.models import *
from application.users.utils import confirm_email, activation_code

users = Blueprint('users', __name__)

################ CREDENTIALITY ROUTES ################
@users.route("/signup", methods=['POST'])
def signup():
    # with complete signup function 

    data = request.get_json()
    # user = User.get_user_by_email(data['email'])
    if User.get_user_by_email(data['email']):
        return jsonify({'message' : 'User already exists'})
    new_user = User(username=data['username'], email=data['email'], password=User.hash_password(data['password']), public_id=str(uuid.uuid4()), activation_code = activation_code)
    
    db.session.add(new_user)
    db.session.commit()

    confirm_email(new_user)
    
    return jsonify({'message':'An email has beeen sent to you to complete your signup'})


@users.route("/complete_signup", methods=['PUT'])
def complete_signup():
    data = request.get_json()
    
    user = User.get_user_by_email(data['email'])
    if user is None:
        return jsonify({'message':'User not found'})

    if user.activation_code == data['code']:
        user.active = True
        user.activation_code = None
        db.session.merge(user)
        db.session.commit()
        return jsonify({'message' : 'You have completed your registration, you can now login'})
    return jsonify({'message':'secret code does not correspond, try again'})


@users.route("/login")
def login():
    pass

@users.route("/forgot_password")
def forgot_password():
    pass

@users.route("/forgot_password/<token>")
def reset_password():
    # login token required
        # password token required
    pass

@users.route("/reset_password")
def reset_request():
    # login token required
    pass

@users.route("/update_pp")
def update_profile():
    # login token required
    pass
################ /CREDENTIALITY ROUTES ################


################ SECRET ROUTE ################
@users.route("/promote_user")
def promote_user():
    # for super_user use only
    pass
################ /SECRET ROUTE ################

################ ADMIN ROUTES ################

@users.route("/delete_user/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    # for admin use only
    new_user = User.get_user_with_id(user_id)
    print(new_user)
    if new_user:
        db.session.delete(new_user)
        db.session.commit()
        return jsonify({'message' : 'User successfully deleted'})
    return jsonify({'message' : 'User not found'})

@users.route("/all_users")
def read_all_users():
    # for admin use only
    pass

@users.route("/create_user")
def create_user():
    # for admin use only
    pass
################ /ADMIN ROUTES ################

