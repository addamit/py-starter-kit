
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

def create_app(flask_config_filename=None):
	app = Flask(__name__)#, instance_relative_config=False)
	#app.config.from_pyfile(flask_config_filename)
	initialize_extensions(app)
	register_blueprints(app)
	
	return app

def register_blueprints(app):
	"""attach blueprints to the flask app"""
	from appy.sample_blueprint import sample_blueprint 
	app.register_blueprint(sample_blueprint)

def initialize_extensions(app):
	"""create default extensions without configuration. """

	db = SQLAlchemy()
	bcrypt = Bcrypt()
	login = LoginManager()

	db.init_app(app)
	bcrypt.init_app(app)
	login.init_app(app)
    

