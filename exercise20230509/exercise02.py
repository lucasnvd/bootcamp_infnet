from time import localtime, strftime, sleep


class User:
    MAX_LOGIN_ATTEMPTS = 3

    def __init__(self, first_name, middle_name, last_name, email):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.blocked_at = None
        self.login_attempts = 0

    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def describe_user(self):
        return print(
            dict(
                first_name=self.first_name,
                middle_name=self.middle_name,
                last_name=self.last_name,
                email=self.email
            )
        )

    def increment_login_attempts(self):
        if self.blocked_at is None:
            self.login_attempts += 1
            if self.login_attempts > User.MAX_LOGIN_ATTEMPTS:
                self.blocked_at = localtime()

            return True
        else:
            return False

    def reset_login_attempts(self):
        if self.blocked_at is not None:
            self.login_attempts = 0
            return True
        else:
            return False

    def greet_user(self):
        print(f"Greetings {self.full_name()}!")

    def hello(self):
        print(self.first_name)


my_user = User(first_name="Matuweuki", middle_name="Xekul", last_name="Rovar", email="matuweuki.rovar92345@gmail.com")

my_user.describe_user()
my_user.greet_user()


def simulate_login(user, attempts=5, delay_in_seconds=1):
    for attempt in range(attempts):
        if user.increment_login_attempts():
            print(f"Attempting to login. Try #{attempt + 1}")
        else:
            print("Ooops... User is blocked...")

        sleep(delay_in_seconds)


def simulate_reset_login_attempts(user):
    if user.reset_login_attempts():
        print("Failed login attempts counter resetted! Now you can sign in again!")
    else:
        print("Cannot reset user login attempts, because he/she is not blocked.")


simulate_login(user=my_user)
simulate_reset_login_attempts(user=my_user)
