from user import User

class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges=privileges
    def show_privileges(self) -> None:
        print('Privileges:', end=' '), print(*self.privileges, sep=', ')

class Admin(User):
    def __init__(self, first_name: str, last_name: str, privileges: Privileges) -> None:
        super().__init__(first_name, last_name)
        self.privileges: Privileges=privileges