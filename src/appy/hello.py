
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path

db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()

def configure_database(app):

	@app.before_first_request
	def initialize_database():
		db.create_all()

	@app.teardown_request
	def shutdown_session(exception=None):
		db.session.remove()

def register_blueprints(app):
	for module_name in ['base']:##, 'd3stories', 'bokehstories'):
		m = 'appy.{}.routes'.format(module_name)
		print ("importing blueprint: {}".format(m))
		module = import_module(m)
		app.register_blueprint(module.blueprint)

def configure_logs(app):
	basicConfig(filename='error.log', level=DEBUG)
	logger = getLogger()
	logger.addHandler(StreamHandler())

def apply_themes(app):
	pass

def create_app(config, selenium = False):
	app = Flask(__name__, static_folder='base/static')
	app.config.from_object(config)
	if selenium:
		app.config['LOGIN_DISABLED'] = True	
	#app.config.from_pyfile(flask_config_filename)
	initialize_extensions(app)
	register_blueprints(app)
	configure_database(app)
	configure_logs(app)
	apply_themes(app)

	
	return app

# def register_blueprints(app):
# 	"""attach blueprints to the flask app"""
# 	from appy.sample_blueprint import sample_blueprint 
# 	app.register_blueprint(sample_blueprint)

def initialize_extensions(app):
	"""create default extensions without configuration. """
	db.init_app(app)
	bcrypt.init_app(app)
	login.init_app(app)
	
