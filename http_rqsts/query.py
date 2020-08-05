import requests
"""QUERY STRINGS: USEFUL FOR PARAMETERIZING GET REQUESTS"""
response = requests.get('https://api.github.com/search/repositories', params={'q': 'requests + language:python'},)

# inspecting some attributes of the 'requests' repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')

"""REQUEST HEADERS: using the headers parameter"""
response = requests.get('https://api.github.com/search/repositories', params={'q': 'requests + language:python'},
                        headers={'Accept': 'application/vnd.github.v3.text-match + json'},)
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')


