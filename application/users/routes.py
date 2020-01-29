from flask import Blueprint, request, jsonify
import uuid
from application.models import *
from application.users.utils import confirm_email

users = Blueprint('users', __name__)

################ CREDENTIALITY ROUTES ################
@users.route("/signup", methods=['POST'])
def signup():
    # with complete signup function 
    data = request.get_json()
    if User.get_user_with_email_and_password(data['email'], data['password']):
        return jsonify({'message' : 'User already exists'})
    new_user = User(username=data['username'], email=data['email'], password=User.hash_password(data['password']), public_id=str(uuid.uuid4()))
    
    db.session.add(new_user)
    db.session.commit()

    confirm_email(new_user)
    
    return jsonify({'message':'An email has beeen sent to you to complete your signup'})


@users.route("/complete_signup", methods=['PUT'])
def complete_signup(token):
    user = user_from_token(token)
    if not user:
        return jsonify({'message':'User not found'})
    user.active = True
    db.session.merge(user)
    db.session.commit()

    return jsonify({'message' : 'You have successfully been Registered, you can now login'})

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

@users.route("/delete_user")
def delete_user():
    # for admin use only
    pass

@users.route("/all_users")
def read_all_users():
    # for admin use only
    pass

@users.route("/create_user")
def create_user():
    # for admin use only
    pass
################ /ADMIN ROUTES ################

