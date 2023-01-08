from flask import Flask,redirect,url_for
from Routes import Login
from Routes.user import User
from config import Config
from dotenv import load_dotenv
def create_app():

    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(Login.bp)
    app.register_blueprint(User.bp)

    @app.route("/")
    def index():
        return "hola mundo"

   
    
    return app 