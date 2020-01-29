import datetime
from marshmallow import fields, validates, ValidationError
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import jwt
import uuid

from application import db, ma, bcrypt
from application.config import Config


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable= False)
    password = db.Column(db.String(150), nullable=False)
    profile_pic = db.Column(db.String(200), default="default.jpg")
    active = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, default=False)
    pics = db.relationship('Pics', backref='user', lazy=True)

    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # updated_on = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"User({self.username}, {self.email}, {len(self.pics)})"

    def __init__(self, username, email, password, public_id):
        self.username = username
        self.email = email
        self.password = User.hash_password(password)
        self.public_id = public_id

    def get_reset_token(self, public_id):
        token = jwt.encode({'public_id': self.public_id, 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, Config.SECRET_KEY)

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password)

    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(Config['SECRET_KEY'], expires_sec)
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None
    
    @staticmethod
    def get_user_with_id(id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user
        else:
            return None
    
    @staticmethod
    def get_user_with_token(token):
        user = User.query.filter_by(token=token).first()
        if user:
            return user
        else:
            return None

class Album(db.Model):
    ___tablename__ = 'album'
    id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String(20), nullable=False, unique=True)
    album_type = db.Column(db.String(20), default='new')
    album_pics = db.relationship('Pics', backref='album', lazy=True)

    
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Album({self.album_name}, {self.album_type}, {self.album_pics})"

    def __init__(self, album_name, album_type, album_pics):
        self.album_name = album_name
        self.album_type = album_type
        self.album_pics = album_pics

class UserSchema(ma.Schema):
    class Meta:
        model = User
        username = fields.String(required=True)
        email = fields.Email(required=True)
        password = fields.String(required=True)
        profile_pic = fields.String()

        @validates('username')
        def validate_username(self, username):
            if len(username) < 5:
                raise ValidationError('Username size too small')
        
        @validates('password')
        def validate_password(self, password):
            if ' ' in password:
                raise ValidationError('Password cannot contain spaces')
            if len(password) < 8:
                raise ValidationError('Password must contain atleast 8 characters')

class Pics(db.Model):
    __tablename__ = 'pics'
    id = db.Column(db.Integer, primary_key=True)
    pic_name = db.Column(db.String(20), nullable=False)
    # pic_album = db.relationship('Album', backref='pics', lazy=True)
    archived = db.Column(db.Boolean, default=False)
    trashed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey(Album.id), nullable=False)

    uploaded_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Pics({self.pic_name}, {self.pic_album}, {self.uploaded_on})"

    def __init__(self, pic_name, pic_album):
        self.pic_name = pic_name
        self.pic_album = pic_album

class PicsSchema(ma.Schema):
    class Meta:
        model = Pics

class AlbumSchema(ma.Schema):
    class Meta:
        model = Album


user_schema = UserSchema()
users_schema = UserSchema(many = True)

Pic_Schema = PicsSchema()
Pics_Schema = PicsSchema(many=True)

album_schema = AlbumSchema()
albums_schema = AlbumSchema(many=True)