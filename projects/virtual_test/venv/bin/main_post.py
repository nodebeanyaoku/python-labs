import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "[YOUR FIRST NAME FIELD]",#add first name inside quotes
    "last_name": "[YOUR LAST NAME FIELD]",#add last name inside quotes
    "email": "[YOUR EMAIL FIELD]"#add email inside quotes
}

response = requests.post(base_url, json=body)

# print the status code (hopefully it's 200 which means all is well)
print(f"Response Code: {response.status_code}")

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your new record?
print(f"Response Content: {response.content}")