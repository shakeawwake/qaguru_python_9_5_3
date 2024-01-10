from data.user_data import user
from pages.registration_page import RegistrationPage

def test_registration():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_form(user=user)
    registration_page.should_registered_user_with(user=user)