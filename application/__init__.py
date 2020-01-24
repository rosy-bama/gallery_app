from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)

    from application.users.routes import users
    from application.pictures.routes import pictures
    app.register_blueprint(users)
    app.register_blueprint(pictures)
    
    return app