from bcrypt import checkpw
from flask import jsonify, render_template, redirect, request, url_for


# from appy import db, login_manager
from appy.base import blueprint
from appy.base.forms import LoginForm, CreateAccountForm

from appy.base.linechart import js, div, cdn_js, cdn_css

@blueprint.route('/')
def route_default():
	current_user = {'username' : 'anonymous' }
	return render_template('plain_page.html', current_user=current_user)

@blueprint.route('/bktest')
def bktest_route():
	current_user = {'username' : 'anonymous' }
	return render_template('plain_page.html', current_user=current_user, 
		js=js, div=div, cdn_js=cdn_js, cdn_css=cdn_css)	

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
	login_form = LoginForm(request.form)
	create_account_form = CreateAccountForm(request.form)

	return render_template('login/login.html', 
		login_form= login_form, 
		create_account_form = create_account_form)
	# login_form = LoginForm(request.form)
	# create_account_form = CreateAccountForm(request.form)
	# if 'login' in request.form:
	# 	username = request.form['username']
	# 	password = request.form['password']
	# 	user = User.query.filter_by(username=username).first()
	# 	if user and checkpw(password.encode('utf8'), user.password):
	# 		login_user(user)
	# 		return redirect(url_for('base_blueprint.route_default'))
	# 	return render_template('errors/page_403.html')
	# if not current_user.is_authenticated:
	# 	return render_template(
	# 		'login/login.html',
	# 		login_form=login_form,
	# 		create_account_form=create_account_form
	# 	)
	# return redirect(url_for('home_blueprint.index'))
