import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 462,
    "first_name": "Geralt",
    "last_name": "Riveria",
    "email": "geraltriveria@yahoo.com"
}

# here we execute the PUT request
response = requests.put(base_url, json=body)
# print the status code (hopefully it's 200 which means all is well)
print(f"Response Code: {response.status_code}")

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your updated record?
print(f"Response Content: {response.content}")