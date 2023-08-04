

class  User:
    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def presentation(self):
        print(f"Hi, my name is {self.username} and I am {self.role}")



class Admin(User):
    def __init__(self, username, email, password):
        super().__init__(username=username, email=email, password=password, role="Admin")
        self.privileges = "A"


class Employee(User):
    def __init__(self, username, email, password):
        super().__init__(username=username, email=email, password=password, role="Employee")
        self.privileges = "B"

