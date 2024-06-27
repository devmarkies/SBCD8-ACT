import os

users = {}

def load_users():
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
#####
def save_users():
    with open("users.txt", "w") as file:
        for username, password in users.items():
            file.write(f"{username},{password}\n")
#####
def register():
    username = input("Enter username: ")
    if username in users:
        print("Already exists.")
        return
    password = input("Enter password: ")
    users[username] = password
    save_users()
    print("Successfully registered.")
#####
def login():
    username = input("Enter username: ")
    if username not in users:
        print(" Does not exist.")
        return
    password = input("Enter password: ")
    if users[username] != password:
        print("Incorrect password.")
        return
    print("Login successful.")
#####
def change_password():
    username = input("Enter username: ")
    if username not in users:
        print("Does not exist.")
        return
    old_password = input("Enter old password: ")
    if users[username] != old_password:
        print("Incorrect old password.")
        return
    new_password = input("Enter new password: ")
    users[username] = new_password
    save_users()
    print("Successfully change.")
#####
while True:
    print("====Welcome to simple login====")
    print("\nSelect an option:")
    print("1. Register")
    print("2. Log in")
    print("3. Change password")
    print("4. Exit")
    
    num = input("Enter ur number: ")
    
    if num == '1':
        register()
    elif num == '2':
        login()
    elif num == '3':
        change_password()
    elif num == '4':
        print("Exit...")
        break
    else:
        print("Invalid choice, please try again.")
