from flask import Blueprint

sample_blueprint = Blueprint('sample_blueprint', __name__)

@sample_blueprint.route('/ex')
def index():
    return "Hello"