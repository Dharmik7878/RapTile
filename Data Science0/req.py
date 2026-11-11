<<<<<<< HEAD
import requests

url = "https://api.github.com/users/octocat"  # Example API endpoint
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data["name"])  # Access data from the JSON
else:
    print(f"Error: {response.status_code}")

# Making a POST request (for sending data to an API):
# data = {"key": "value"}
# response = requests.post(url, json=data)  # Sends data as JSON

=======
import requests

url = "https://api.github.com/users/octocat"  # Example API endpoint
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data["name"])  # Access data from the JSON
else:
    print(f"Error: {response.status_code}")

# Making a POST request (for sending data to an API):
# data = {"key": "value"}
# response = requests.post(url, json=data)  # Sends data as JSON

>>>>>>> 0be82eea013b4a95ecf7d92f4bd55fb50d4253d3
# Other HTTP methods: put(), delete(), etc.