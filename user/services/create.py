from user.models import User


class CreateUserService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create(self):
        return User.objects.create_user(
            username=self.username,
            password=self.password
        )
