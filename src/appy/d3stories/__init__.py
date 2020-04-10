from flask import Blueprint

d3_blueprint = Blueprint(
	'd3_blueprint', 
	__name__,
	url_prefix='/d3',
    template_folder='templates',
    static_folder='static')