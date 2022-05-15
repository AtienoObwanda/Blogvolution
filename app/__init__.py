from flask import Flask
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask_mail import Mail
from flask_bootstrap import Bootstrap


from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    # db.init_app(app)
    # login_manager.init_app(app)

    # Will add the views and forms
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # create login view function
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    return app