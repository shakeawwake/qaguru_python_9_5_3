from selene import browser, have, by
from picture import resources
from data.user_data import User


class RegistrationPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_form(self, user: User):
        browser.element('#firstName').type(user.name).press_enter()
        browser.element('#lastName').type(user.lastname)
        browser.element('#userEmail').type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.phone)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(user.birthday_month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(user.birthday_year)).click()
        browser.element(
            f'.react-datepicker__day--0{user.birthday_day}:not(.react-datepicker__day--outside-month)'
        ).click()
        browser.element('[for="hobbies-checkbox-1"]').click()

        browser.element('#subjectsInput').type('En')
        browser.element('#react-select-2-option-0').should(have.exact_text(user.subject)).click()

        browser.element('#uploadPicture').send_keys(resources.path(user.picture))
        browser.element('[placeholder="Current Address"]').type(user.address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.name} {user.lastname}',
                user.email,
                user.gender,
                user.phone,
                f'{user.birthday_day} {user.birthday_month},{user.birthday_year}',
                user.subject,
                user.hobby,
                user.picture,
                user.address,
                f'{user.state} {user.city}'
            )
        )
