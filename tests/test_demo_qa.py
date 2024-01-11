from pages.registration_page import RegistrationPage


def test_demo_qa(settings):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('TestName')
    registration_page.fill_last_name('TestLastName')
    registration_page.fill_email("test@user.test")
    registration_page.choice_gender()
    registration_page.fill_user_number("8916506361")
    registration_page.fill_date_of_birth('1994', 'July', '03')
    registration_page.fill_subjects('En')
    registration_page.fill_hobbies()
    registration_page.upload_picture('logo.png')
    registration_page.fill_current_address('TestAdress')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Gurg')
    registration_page.click_submit()

    # THEN
    registration_page.should_registered_user_with(
        'TestName TestLastName',
        'test@user.test',
        'Female',
        '8916506361',
        '03 July,1994',
        'English',
        'Sports',
        'logo.png',
        'TestAdress',
        'NCR Gurgaon'
    )
