from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from application.config import Config

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    bcrypt = Bcrypt(app)

    from application.users.routes import users
    from application.pics.routes import pics
    from application.albums.routes import albums
    from application.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(pics)
    app.register_blueprint(albums)
    app.register_blueprint(main)
    
    return app