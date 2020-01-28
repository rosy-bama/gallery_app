from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/search_pic/<date_or_name>")
def search_pic():
    # search by upload date or album name
    pass

@main.route("/search_album/<date_or_Sname>")
def search_album():
    # search by upload date or album name
    pass

@main.route("/create_trash")
def create_trash():
    pass

@main.route("/create_archive")
def create_archive():
    pass