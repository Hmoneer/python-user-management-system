import json

class UserSystem:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except:
            self.users = {}

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def register(self):
        username = input("Enter username: ")
        
        if username in self.users:
            print("Username already exists!")
            return
        
        password = input("Enter password: ")
        self.users[username] = password
        self.save_users()
        print("User registered successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in self.users and self.users[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password")

    def menu(self):
        while True:
            print("\n1- Register")
            print("2- Login")
            print("3- Exit")
            
            choice = input("Choose: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")


system = UserSystem()
system.menu()