import unittest
import appy
 

import pytest
def test_home_page(test_client):
	response = test_client.get('/ex')
	print ("DATA:{}".format(response.data))
	assert response.status_code == 200
	assert response.data == b'Hello'
