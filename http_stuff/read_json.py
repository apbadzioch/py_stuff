import requests
import json
from http import HTTPStatus # better to use this over hardcoding status number (200, 404, ...)

# user_name = input("Enter your username: ")
# url = f"https://api.github.com/users/{user_name}"
site = input("enter site url: ")
url = f"https://{site}"
response = requests.get(url)
response.raise_for_status()
#data = response.json()
data = response.text

if response.status_code == HTTPStatus.OK:
    print(data)
else:
    print(f"failure. status code: {response.status_code}")