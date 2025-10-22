import requests


import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/ 

get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": "abc134"}) # HTTP Request
# print(get_response.headers)
# print(get_response.text) # print raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
print(get_response.json())
# print(get_response.status_code)


# endpoint = "https://httpbin.org/anything" 


# #application
# get_response = requests.get(endpoint) #http requests #API=>method
# print(get_response.text) #print raw text res
# print(get_response.json()) #print python Dict
# # {
# #   "args": {}, 
# #   "data": "", 
# #   "files": {}, 
# #   "form": {}, 
# #   "headers": {
# #     "Accept": "*/*", 
# #     "Accept-Encoding": "gzip, deflate", 
# #     "Host": "httpbin.org", 
# #     "User-Agent": "python-requests/2.32.5", 
# #     "X-Amzn-Trace-Id": "Root=1-68f75b65-57d05f900db538d445a02008"
# #   }, 
# #   "json": null, 
# #   "method": "GET", 
# #   "origin": "212.34.13.136", 
# #   "url": "https://httpbin.org/anything"
# # }
# # javaScrpit Object Notations ~ python Dict
# print(get_response.json()) #print python Dict
# # {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.5', 'X-Amzn-Trace-Id': 'Root=1-68f75d2a-30128e9e053cafc6453b7389'}, 'json': None, 'method': 'GET', 'origin': '212.34.13.136', 'url': 'https://httpbin.org/anything'}


