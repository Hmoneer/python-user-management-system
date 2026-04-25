class UserSystem:
    def __init__(self):
        self.users = {}

    def register(self):
        username = input("Enter username: ")
        
        if username in self.users:
            print("Username already exists!")
            return
        
        password = input("Enter password: ")
        self.users[username] = password
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


# تشغيل البرنامج
system = UserSystem()
system.menu()