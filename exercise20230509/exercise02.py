class User:
    def __init__(self, first_name, middle_name, last_name, email):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email

    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def describe_user(self):
        return dict(
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            email=self.email
        )

    def greet_user(self):
        print(f"Greetings {self.full_name()}!")

    def hello(self):
        print(self.first_name)


my_user = User(first_name="Lucas", middle_name="Nao", last_name="Sei", email="lucas.naosei@gmail.com")
print(my_user.describe_user())

my_user.greet_user()
