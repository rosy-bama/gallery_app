from flask import Blueprint

albums = Blueprint('albums', __name__)

############## ADMIN ROUTES ##############
@albums.route("/all_albums")
def all_albums():
    pass

############## ADMIN ROUTES ##############

@albums.route("/new_album")
def create_album():
    pass

@albums.route("/album/<album_id>")
def read_an_album():
    pass

@albums.route("/my_albums")
def read_my_albums():
    pass

@albums.route("/update_album/<album_id>")
def update_album():
    # we can rename
    # mark as favorite by fav=True
    pass

@albums.route("/archive_album/<album_id>")
def archive_album():
    pass

@albums.route("/delete_album/<album_id>")
def delete_album():
    # move to trash, to delete permanently empty trash
    pass
