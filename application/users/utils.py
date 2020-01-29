from application import mail
from application.models import User
from application.config import Config

from flask_mail import Message
from flask import url_for

def confirm_email(user):
    token = user.get_reset_token(user)
    msg = Message("Email Confirmation", sender=Config.MAIL_USERNAME, recipients=[user.email])
    msg.body = f'''Hey dear {user.username}, please visit the following link to confirm your Email and complete your signup on GALLERY_APP:
{url_for('users.complete_signup', token=token, _external=True)}

Simply ignore this message if you did not make such a request.
    '''

def user_from_token(token):
    try:
        data = jwt.decode(token, Config.SECRET_KEY)
        public_id = data['public_id']
    except:
        return None
    get_user_with_id(public_id)