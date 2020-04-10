from flask import Blueprint

bk_blueprint = Blueprint(
	'bk_blueprint', 
	__name__,
	url_prefix='/bk',
    template_folder='templates',
    static_folder='static')