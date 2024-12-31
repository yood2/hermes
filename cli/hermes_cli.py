import requests

BASE_URL = "http://127.0.0.1:8000"

def cli():
    print('''

         _       _    _            _          _   _         _           _        
        / /\    / /\ /\ \         /\ \       /\_\/\_\ _    /\ \        / /\      
       / / /   / / //  \ \       /  \ \     / / / / //\_\ /  \ \      / /  \     
      / /_/   / / // /\ \ \ \     / /\ \ \   /\ \/ \ \/ / // /\ \ \    / / /\ \__  
     / /\ \__/ / // / /\ \_\   / / /\ \_\ /  \____\__/ // / /\ \_\  / / /\ \___\ 
    / /\ \___\/ // /_/_ \/_/  / / /_/ / // /\/________// /_/_ \/_/  \ \ \ \/___/ 
   / / /\/___/ // /____/\    / / /__\/ // / /\/_// / // /____/\      \ \ \       
  / / /   / / // /\____\/   / / /_____// / /    / / // /\____\/  _    \ \ \      
 / / /   / / // / /______  / / /\ \ \ / / /    / / // / /______ /_/\__/ / /      
/ / /   / / // / /_______\/ / /  \ \ \\/_/    / / // / /_______\\ \/___/ /       
\/_/    \/_/ \/__________/\/_/    \_\/        \/_/ \/__________/ \_____\/        
                                                                                 

''')
    input("Press Enter to continue...")
    
    while True:
        print('''
    Welcome to Hermes CLI.

    Select an option:
    1. Create a new user
    2. Get user data
    9. Exit
            ''')
        option = input("Enter an option: ")
        if option == "1":
            create_user()
            input("Press Enter to continue...")
        elif option == "2":
            get_user()
            input("Press Enter to continue...")
        elif option == "9":
            exit()
        else:
            print("Invalid option")

def create_user():
    name = input("Enter a user name: ")
    response = requests.post(f"{BASE_URL}/users", json={
        "name": name
    })
    print(response.json())

def get_user():
    name = input("Enter a user name: ")
    response = requests.get(f"{BASE_URL}/users/{name}")
    print(response.json())

if __name__ == "__main__":
    cli()
