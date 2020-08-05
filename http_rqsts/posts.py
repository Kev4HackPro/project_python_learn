import requests

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
json_response = response.json()
dict_values = json_response['data']
print(dict_values)
type_content = json_response['headers']['content-type']
print(type_content)
