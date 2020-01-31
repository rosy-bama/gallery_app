from application import mail
from application.models import User
from application.config import Config

from flask_mail import Message
from flask import url_for
import secrets

activation_code = secrets.token_hex(6)

def confirm_email(user):
    token = user.get_reset_token(user)
    msg = Message(subject="Email Confirmation", sender=Config.MAIL_USERNAME, recipients=[user.email])
    msg.body = f'''
    Hey dear {user.username}, You're almost done! Please enter the code below into our app to confirm your Email:
{activation_code}

    Simply ignore this message if you did not make such a request.
    '''

    mail.send(msg)

def user_from_token(token):
    try:
        data = jwt.decode(token, Config.SECRET_KEY)
        public_id = data['public_id']
    except:
        return None
    get_user_with_id(public_id)