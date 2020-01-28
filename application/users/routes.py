from flask import Blueprint
import application.models

users = Blueprint('users', __name__)

################ CREDENTIALITY ROUTES ################
@users.route("/signup")
def signup():
    # with complete signup function 
    pass

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

