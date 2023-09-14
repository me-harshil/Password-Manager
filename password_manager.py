import random
import string

class PasswordManager:
    def __init__(self):
        self.password_dict = {}
        try:
            with open("passwords.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    name, password, comment = line.split(":")
                    self.password_dict[name] = password
        except FileNotFoundError:
            with open("passwords.txt", "w") as f:
                pass

    def show_all_password_dict(self):
        with open("passwords.txt", "r") as f:
            print("\nAll passwords:\n")
            for line in f:
                name, password, comment = line.split(":")
                self.password_dict[name] = password
                print(f"{name}: {password} , comment:{comment}", end="")

    def get_password(self, name):
        if name in self.password_dict:
            return self.password_dict[name]
        else:
            print(f"No password found for {name}")

    def update_password(self, name, password):
        if name in self.password_dict:
            file = open('passwords.txt', 'r')
            content = file.read()
            new_content = content.replace(self.password_dict[name], password)
            file.close()
            file = open('passwords.txt', 'w')
            file.write(new_content)
            file.close()
            self.password_dict[name] = password
            print(f"Password for {name} updated")
        else:
            print(f"No password found for {name}")

    def add_new_password(self, name, password, comment=""):
        if name in self.password_dict:
            print(f"Password for {name} already exists")
        else:
            self.password_dict[name] = password
            print(f"Password for {name} added")
            with open("passwords.txt", "a") as f:
                f.write(f"{name}:{password}:{comment}\n")
            if comment:
                print(f"Comment: {comment}")

    def generate_password(self, length=12):
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        password = ''.join(random.choice(letters + digits + symbols)
                           for _ in range(length))
        return password


pm = PasswordManager()

while True:
    print("""What would you like to do?
    1. Show all passwords
    2. Get a password
    3. Update a password
    4. Add a new password
    5. Generate a new password
    6. Quit""")
    choice = input("Enter your choice (1-6): ")

    match choice:
        case "1":
            pm.show_all_password_dict()
        case "2":
            name = input(
                "Enter the name for which you want to get the password: ")
            password = pm.get_password(name)
            if password:
                print(f"Password for {name}: {password}")
        case "3":
            name = input(
                "Enter the name for which you want to update the password: ")
            password = input("Enter the new password: ")
            pm.update_password(name, password)
        case "4":
            name = input(
                "Enter the name for which you want to add a new password: ")
            password = input("Enter the new password: ")
            comment = input("Enter a comment (optional): ")
            pm.add_new_password(name, password, comment)
        case "5":
            length = int(input("Enter the length of the password: "))
            password = pm.generate_password(length)
            print(f"Generated password: {password}")
            name = input("Enter a name for the new password: ")
            comment = input("Enter a comment (optional): ")
            pm.add_new_password(name, password, comment)
        case "6":
            print("Thank you for using the password manager. Goodbye.")
            exit()
        case _:
            print("Invalid choice. Please enter a number between 1 and 6.")
