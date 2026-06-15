import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url=api_url)
# Check if the request was successful (Status Code 200)
for key,value in response.json().items():
    if key == "completed":
        if value == False:
            print("The data is not completed in server")
print(response.json())
