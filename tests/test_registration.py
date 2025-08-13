import pytest
from playwright.sync_api import Page

from pages.dashboard_page import DashBoardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration( dashboard_page: DashBoardPage, registration_page: RegistrationPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form(
            email="email",
            username="username",
            password="password"
        )
        registration_page.click_registration_button()

        dashboard_page.check_dashboard_visible_title()
