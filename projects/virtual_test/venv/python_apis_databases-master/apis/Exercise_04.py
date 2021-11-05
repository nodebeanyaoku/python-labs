'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''


import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 464,
    "first_name": "JOHNNY",#add first name inside quotes
    "last_name": "QUEST",#add last name inside quotes
    "email": "Johnny.quest@quest.co"#add email inside quotes
}


response = requests.put(base_url, json=body)

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your new record?
print(f"Response Content: {response.content}")