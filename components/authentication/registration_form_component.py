from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.identifier = identifier

        self.email = Input(page, '{identifier}-email-input', 'Email')
        self.username = Input(page, '{identifier}-username-input', 'Username')
        self.password = Input(page, '{identifier}-password-input', 'Password')

    def fill_registration_form(self, email: str, password: str, username: str):
        self.email.fill(email, identifier=self.identifier)
        self.username.fill(username, identifier=self.identifier)
        self.password.fill(password, identifier=self.identifier)

    def check_visible(self):
        self.email.check_visible(identifier=self.identifier)
        self.email.check_have_text("user@gmail.com", identifier=self.identifier)

        self.username.check_visible(identifier=self.identifier)
        self.username.check_have_text("username", identifier=self.identifier)

        self.password.check_visible(identifier=self.identifier)