import requests
from http import HTTPStatus # better to use this over hardcoding status number (200, 404, ...)
from requests import HTTPError
from pprint import pprint

username = "apbadzioch"
#repo = "py_stuff"
url = f"https://api.github.com/users/{username}/repos"

# url = 'https://swapi.info/api/films'

response = requests.get(url)
response.raise_for_status()
data = response.json()
#data = response.content

if response.status_code == HTTPStatus.OK:
    for d in data:
        repo_id = d.get('id')
        repo_name = d.get('name')
        print(f'id: {repo_id} | name: {repo_name}')
    #print(data['id'])
else:
    print(f"failure. status code: {response.status_code}")