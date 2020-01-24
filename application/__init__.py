from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)

    from application.users.routes import users
    from application.pics.routes import pics
    from application.albums.routes import albums
    app.register_blueprint(users)
    app.register_blueprint(pics)
    app.register_blueprint(albums)
    
    return app