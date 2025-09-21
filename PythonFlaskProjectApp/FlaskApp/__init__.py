from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///.hot2.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
    app.secret_key = 'hot'
    db.__init__(app)

    with app.app_context():
        db.create_all()


    from .auth import auth as auth_blueprint

    from .main import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app