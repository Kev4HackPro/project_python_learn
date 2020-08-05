import requests
from requests.exceptions import HTTPError

"""SIMPLE GET REQUEST AND STATUS CODES"""
response = requests.get('https://www.google.com')
status = response.status_code
if response.status_code == 200:
    print('Success! you got through')
elif response.status_code == 404:
    print('Resource you looking for cannot be found`')

# or
# This method however does not verify that the status code is 200
# It states that status codes in range 200 - 400 are successful

if response:
    print('Success')
else:
    print('An error occurred')

for url in ['https://www.duckduckgo.com', 'https://www.bing.com']:
    try:
        response = requests.get(url)

        # if response was successful
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
"""ACCESSING GET CONTENT"""
response = requests.get('https://www.google.com')
byte_content = response.content  # prints out content in bytes
str_content = response.text  # the content here is actually serially serialized JSON content
print(str_content)
# to get a dict, you could take the str you retrieved from.text and deserialize it using json.loads()
# or a simpler way we can use .json()
deserialize = response.json()
print(deserialize)  # content here is a dictionary, so one can access values in the object by key

"""HEADERS"""
headers = response.headers  # .headers returns a dictionary-like object allowing you to access header values by key
print(headers)
content_type = response.headers['Content-Type']  # value being accessed is not case sensitive
print(content_type)
