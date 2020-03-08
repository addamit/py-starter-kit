from unittest.mock import Mock, patch

import pytest
import appy


def test_external_call():

	sample_data = {'content' : [1, 2, 3]}
	with patch('appy.external_data.requests.get') as mock_get:
		mock_get.return_value = Mock(ok=True)
		mock_get.return_value.json.return_value = sample_data
		mock_get.return_value.status_code = 'ok'
		
		results = appy.external_data.get_data() 
		assert results.json() == sample_data
		assert results.status_code == 'ok'


def test_external_call_explicit_control():
	"""Shows explicit control of mocking - when to start and stop. 
	Can be used for fine grained control
	"""

	sample_data = {'content' : [1, 2, 3]}
	mock_get_patcher = patch('appy.external_data.requests.get')
	# start mocking
	mock_get = mock_get_patcher.start()
	mock_get.return_value = Mock()
	mock_get.return_value.json.return_value = sample_data
	# call the api
	results = appy.external_data.get_data() 

	# stop mocking 
	mock_get_patcher.stop()

	assert results.json() == sample_data
		

def test_external_using_fixture(mocked_external_get):

	"""This test method uses a fixture that is patched http request mock object.

	Useful for using across multiple tests.
	"""
	sample_data = {'data' : [1, 2, 3]}
	results = appy.external_data.get_data() 
	assert results.json() == sample_data

def test_external_using_fixture2(mocked_external_get):

	"""This test method uses a fixture that is patched http request mock object.

	Useful for using across multiple tests.
	"""
	sample_data = {'data' : [1, 2, 3]}
	results = appy.external_data.get_data() 
	assert results.json()['data'] == [1, 2, 3]


def test_real_call(mocked_external_get):
	""" The fixture affects this test case as well. 
	TODO: Need to remove the mock from fixture explicitly"""

	mocked_external_get.stop() # this does not turn off mocking. Need to verify
	results = appy.external_data.get_data() 
	j = results.json()
	print (j)
	assert 'page' in j == True

