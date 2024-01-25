import json
from enum import Enum
from typing import Any

from playwright.sync_api import expect
from pages.MainPage import MainPage


class UserType(Enum):
    STANDARD_USER = "standard_user"
    LOCKED_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"


class LoginPage(MainPage):
    # ELEMENTS
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"

    def __init__(self,
                 driver: Any,
                 user: UserType = UserType.STANDARD_USER,
                 creds_filepath: str = "../config/creds.json"):
        super().__init__(driver)
        self.page = driver
        self.credentials = UserCredentials(creds_filepath)
        self.login(user=user)

    def login(self, user: UserType) -> None:
        password = self.credentials.get_password_for_user(user.value)
        self.page.locator(self.USERNAME_INPUT).type(user.value)
        self.page.locator(self.PASSWORD_INPUT).type(password)
        self.page.locator(self.LOGIN_BUTTON).press('Enter')
        expect(self.page.get_by_text("Swag Labs")).to_be_visible()


class UserCredentials:
    def __init__(self, filepath: str):
        with open(filepath) as f:
            self.config = json.load(f)

    def get_password_for_user(self, user: str) -> str:
        for user_info in self.config["users"]:
            if user_info["username"] == user:
                return user_info["password"]
        raise Exception("User credentials not found")
