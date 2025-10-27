import requests   # imports the HTTP requests library

# sends a GET request to GitHub’s public API
response = requests.get("https://api.github.com")

# prints HTTP status code (200 = success)
print("Status Code:", response.status_code)

# prints the response data in JSON format
print("Response:", response.json())



