from flask import Blueprint

pics = Blueprint('pics', __name__)

############## ADMIN ROUTES ##############
@pics.route("/all_pics")
def all_pics():
    pass
############## ADMIN ROUTES ##############

@pics.route("/upload_pic")
def upload_pic():
    pass

@pics.route("/pic/<pic_id>")
def read_a_pic():
    pass

@pics.route("/my_pics")
def all_my_pics():
    # this is what shows all pics, sorted by upload date
    pass

@pics.route("/update_pic/<pic_id>")
def update_pic():
    # here we can rename
    # mark as favorite
    # move to another album by pic.album = data.album
    pass

@pics.route("/archive_pic/<pic_id>")
def archive_pic():
    pass

@pics.route("/delete_pic/<pic_id>")
def delete_a_pic():
    # move to trash
    pass

@pics.route("/delete_pics")
def delete_all_pics():
    # move all pics to recycle bin in their respective named album
    # when we restore these, and read them, they should still be sorted by upload date
    # to delete permanently we need to empty the trash
    pass