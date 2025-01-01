import requests

BASE_URL = "http://127.0.0.1:8000"

def cli():
    print('''
    Welcome to Hermes CLI.

    Select an option:
    1. Create a new user
    2. Get user data
    9. Exit
''')
    
    while True:
        option = input("Enter an option: ")
        if option == "1":
            create_user()
        elif option == "2":
            get_user()
        elif option == "9":
            exit()
        else:
            print("Invalid option")

def create_user():
    user_id = input("Enter a user ID: ")
    try:
        response = requests.post(f"{BASE_URL}/users", json={"user_id": user_id})
        if response.status_code >= 400:
            error_data = response.json()
            print("\n❌ Error creating user:")
            print(f"Status code: {response.status_code}")
            print(f"Detail: {error_data.get('detail', 'Unknown error')}\n")
        else:
            print("\n✅ User created successfully:")
            print(response.json(), "\n")
    except requests.RequestException as e:
        print(f"\n❌ Connection error: {str(e)}\n")

def get_user():
    user_id = input("Enter a user ID: ")
    try:
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        if response.status_code >= 400:
            error_data = response.json()
            print("\n❌ Error retrieving user:")
            print(f"Status code: {response.status_code}")
            print(f"Detail: {error_data.get('detail', 'Unknown error')}\n")
        else:
            print("\n✅ User found:")
            print(response.json(), "\n")
    except requests.RequestException as e:
        print(f"\n❌ Connection error: {str(e)}\n")

if __name__ == "__main__":
    cli()
