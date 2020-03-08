
from unittest.mock import Mock, patch

import sys
from pathlib import Path
# `path.parents[1]` is the same as `path.parent.parent`
d = Path(__file__).resolve().parents[1]
src_path = Path.joinpath(d, "src")
sys.path.insert(0,  str(src_path))

import pytest

from appy import hello
import appy


@pytest.fixture(scope='module')
def test_client():
	flask_app = hello.create_app()
	flask_app.config['TESTING'] = True
	testing_client = flask_app.test_client()
	# Establish an application context before running the tests.
	ctx = flask_app.app_context()
	ctx.push()
 
	yield testing_client  # this is where the testing happens!
 
	ctx.pop()


# below affects all tests in the test module
#@pytest.fixture(scope='module')
@pytest.fixture
def mocked_external_get():

	sample_data = {'data' : [1, 2, 3]}

	mock_get_patcher = patch('appy.external_data.requests.get')
	# start mocking
	mock_get = mock_get_patcher.start()

	mock_get.return_value = Mock()
	mock_get.return_value.json.return_value = sample_data

	yield mock_get

	mock_get.stop()

