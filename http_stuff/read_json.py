import requests
from http import HTTPStatus # better to use this over hardcoding status number (200, 404, ...)
from requests import HTTPError

# user_name = input("Enter your username
#site = input("enter site url: ")
#url = f"https://{site}"

url = 'https://swapi.info/api/films'

response = requests.get(url)
response.raise_for_status()
#data = response.json()
data = response.content

if response.status_code == HTTPStatus.OK:
    print(data.decode())
else:
    print(f"failure. status code: {response.status_code}")