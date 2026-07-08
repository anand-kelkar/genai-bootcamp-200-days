import requests
import json

api_response = requests.get('https://jsonplaceholder.typicode.com/users')

users = json.loads(api_response.text)
print(type(users))
for user in users:
    print (f"User Name : {user["username"]} , Email : {user["email"]} , Company : {user["company"]["name"]}")