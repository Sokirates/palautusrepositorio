from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if self._user_repository.find_by_username(username):
            raise ValueError("username already exists")
        
        if len(username) < 3:
            raise ValueError("Username should be at least 3 letters long")

        if re.match("^[a-z]+$", username) is None:
            raise ValueError("Username should contain only lowercase letters")

        if len(password) < 8 is None:
            raise ValueError("Password should be at least 8 letters long")

        if re.match(".*[^a-z].*", password) is None:
            raise ValueError("Password should not contain only letters")