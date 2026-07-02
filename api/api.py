import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print(type(response))
print(response)

data = response.json()

print(type(data))
print(data)