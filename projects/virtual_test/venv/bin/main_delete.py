import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.delete(base_url + "/462")
print(response.status_code)


# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your updated record?
print(f"Response Content: {response.content}")