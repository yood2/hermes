import requests

# Define the API URL (adjust the base URL and prefix as needed)
API_URL = "http://127.0.0.1:8000/users/"

# Define the payload
user_data = {
    "user_id": "12345",
    "portfolio": {}
}

# Make the POST request
response = requests.post(API_URL, json=user_data)

# Handle the response
if response.status_code == 200:
    print("User created successfully!")
    print("Response:", response.json())
else:
    print("Failed to create user.")
    print("Status code:", response.status_code)
    print("Error:", response.json())
