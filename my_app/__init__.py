from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app(config_classname):
    """
    Initialise the Flask application.
    :type config_classname: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """

    app = Flask(__name__)
    # login_manager.init_app(app) # Leave this commented until we enable the login functionality

    app.config.from_object(config_classname)
    csrf.init_app(app)
    db.init_app(app)


    from my_app.community.community import community_bp
    app.register_blueprint(community_bp)

    from my_app.main.main import main_bp
    from my_app.community.community import community_bp
    from my_app.auth.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(community_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        from dash_app.dash import init_dashboard
        app = init_dashboard(app)

        from my_app.models import User
        db.create_all()



    return app
