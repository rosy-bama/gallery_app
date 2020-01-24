from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/search_pic/<date or name>")
def search_pic():
    # search by upload date or album name
    pass

@main.route("/search_album/<date or name>")
def search_album():
    # search by upload date or album name
    pass

@main.route("/create_trash")
def create_trash():
    pass

@main.route("/create_archive")
def create_archive():
    pass