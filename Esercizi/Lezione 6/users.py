class User:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str=first_name
        self.last_name: str=last_name
        self.login_attempts: int=0
    def describe_user(self) -> None:
        print(f'First name: {self.first_name}, Last name: {self.last_name}')
    def greet_user(self) -> None:
        print(f'Hello {self.first_name} {self.last_name}')
    def increment_login_attempts(self, new_login_attempts: int) -> None:
        self.login_attempts+=new_login_attempts
    def reset_login_attempts(self) -> None:
        self.login_attempts=0

class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges=privileges
    def show_privileges(self) -> None:
        print('Privileges:', end=' '), print(*self.privileges, sep=', ')

class Admin(User):
    def __init__(self, first_name: str, last_name: str, privileges: Privileges) -> None:
        super().__init__(first_name, last_name)
        self.privileges: Privileges=privileges