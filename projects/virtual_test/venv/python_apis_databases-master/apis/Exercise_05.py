'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''


import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"




response = requests.delete(base_url + "/464")

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your new record?
print(f"Response Content: {response.content}")