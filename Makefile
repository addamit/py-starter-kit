MKDIR = mkdir
SRC_DIR=appy
SRC_SETTINGS=APPY
TEMPLATES_DIR=templates
STATIC_DIR=static
TEST_DIR=tests
PKG_VERSION="1.0.0"


init:
	@echo "\033[92mCREATING DIRECTORY STRUCTURE..\033[0m"
	for fdname in $(SRC_DIR) $(TEST_DIR) $(SRC_DIR)/$(STATIC_DIR) $(SRC_DIR)/$(TEMPLATES_DIR) ; do \
		echo $$fdname; \
		$(MKDIR) $$fdname;  \
	done

	@echo "\033[92mCREATING MANIFEST..\033[0m"

	echo "recursive-include $(SRC_DIR)/$(TEMPLATES_DIR) *" >> MANIFEST.in
	echo "recursive-include $(SRC_DIR)/$(STATIC_DIR) *" >> MANIFEST.in

	@echo "\033[92mCREATING settings.cfg ..\033[0m"
	echo "DEBUG = True" >> settings.cfg

	@echo "\033[92mCREATING __init__.py ..\033[0m"
	touch $(SRC_DIR)/__init__.py

	echo "__VERSION__ = \"$(PKG_VERSION)"\" >> $(SRC_DIR)/__init__.py 

	echo "import os" >> $(SRC_DIR)/__init__.py 
	echo "from flask import Flask" >> $(SRC_DIR)/__init__.py
	echo "app = Flask(__name__)" >> $(SRC_DIR)/__init__.py
	echo "app.config.from_object('$(SRC_DIR).default_settings')" >> $(SRC_DIR)/__init__.py
	#app.config.from_envvar('APP_SETTINGS')
	echo "app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0" >> $(SRC_DIR)/__init__.py

	echo "if not app.debug:" >> $(SRC_DIR)/__init__.py
	echo "    import logging" >> $(SRC_DIR)/__init__.py
	echo "    from logging.handlers import TimedRotatingFileHandler" >> $(SRC_DIR)/__init__.py
	echo "    file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'app.log'), 'midnight')" >> $(SRC_DIR)/__init__.py
	echo "    file_handler.setLevel(logging.WARNING)" >> $(SRC_DIR)/__init__.py
	echo "    file_handler.setFormatter(logging.Formatter('<% (asctime(s> <%(levelname)s> %(message)s'))" >> $(SRC_DIR)/__init__.py
	echo "    app.logger.addHandler(file_handler)" >> $(SRC_DIR)/__init__.py

	echo "import $(SRC_DIR).views" >> $(SRC_DIR)/__init__.py

	@echo "\033[92mCreating default settings.\033[0m"
	echo "DEBUG = False" >> $(SRC_DIR)/default_settings.py	
	echo "LOG_DIR = '.'" >> $(SRC_DIR)/default_settings.py


	@echo "\033[92mCreating starter view.\033[0m"
	echo "import json" >> $(SRC_DIR)/views.py
	echo "from flask import render_template" >> $(SRC_DIR)/views.py
	echo "from $(SRC_DIR) import app" >> $(SRC_DIR)/views.py
	echo " " >> $(SRC_DIR)/views.py >> $(SRC_DIR)/views.py
	echo "@app.route('/')" >> $(SRC_DIR)/views.py 
	echo "def index():" >> $(SRC_DIR)/views.py
	echo "    app.logger.info('index access')" >> $(SRC_DIR)/views.py
	echo "    return render_template('index.html')" >> $(SRC_DIR)/views.py

	

	@echo "\033[92mCreating index page.\033[0m"

	echo "Hello World" >> $(SRC_DIR)/$(TEMPLATES_DIR)/index.html

	@echo "\033[92mDONE.\033[0m"




clean:
	rm -rf $(SRC_DIR)
	rm -rf $(TEST_DIR)
	rm MANIFEST.in
	echo Done


.PHONY: all

all: 
	echo 'executing run command'

mkenv:
	virtualenv venv

setup: 
	( \
		source venv/bin/activate; \
		python setup.py develop; \
	)	

flakes:
	find $(SRC_DIR) -name "*.py" | egrep -v '^./tests/' | xargs pyflakes

lint:
	find $(SRC_DIR) -name "*.py" | egrep -v '^./tests/' | xargs pylint --output-format=parseable --report=y > pylint.log

run: setup
	FLASK_APP=$(SRC_DIR) $(SRC_SETTINGS)_SETTINGS=../settings.cfg venv/bin/flask run

test: setup
	$(SRC_SETTINGS)_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist:
	venv/bin/python setup.py sdist




