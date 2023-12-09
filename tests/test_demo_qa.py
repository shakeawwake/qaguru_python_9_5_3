import os.path

from selene import browser, be, have, by


def test_demo_qa(start_settings_google):

    browser.open("/automation-practice-form")
    browser.element('[id="firstName"]').type("TestName").press_enter()
    browser.element('[id="lastName"]').type("TestLastName").press_enter()
    browser.element('[id="userEmail"]').type("test@user.test").press_enter()
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').type("89165063611")
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element(by.text("July")).click()
    browser.element('[class="react-datepicker__year-select"]').click().element(by.text("1994")).click()
    browser.element('[aria-label="Choose Sunday, July 3rd, 1994"]').click()
    browser.element('[id="subjectsInput"]').type("En").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath("logo.png"))
    browser.element('[placeholder="Current Address"]').type("TestAdress")
    browser.element('[id="react-select-3-input"]').type("NCR").press_enter()
    browser.element('[id="react-select-4-input"]').type("Gurg").press_enter()
    browser.element('[id="submit"]').press_enter()

    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'TestName TestLastName',
            'test@user.test"',
            'Female',
            '89165063611',
            '03 July,1994',
            'English',
            'Sports',
            'logo.jpg',
            'TestAdress',
            'NCR Gurgaon'
        )
    )