import requests

def get_data():
	response = requests.get('https://reqres.in/api/users?page=2')
	return response
	# if response.status_code == 200:
	# 	print (response.json())
	# 	# return response.json()
	# 	return response

if __name__ == '__main__':
	r = get_data()
	print (r.status_code)
	print (r.json())
