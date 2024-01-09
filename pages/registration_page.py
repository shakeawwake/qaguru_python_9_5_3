from selene import browser, by, have
from picture import resources

class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, name):
        browser.element('#firstName').type(name).press_enter()

    def fill_last_name(self, lastname):
        browser.element('#lastName').type(lastname).press_enter()

    def fill_email(self, email):
        browser.element('#userEmail').type(email).press_enter()

    def choice_gender(self):
        browser.element('#gender-radio-2').double_click()

    def fill_user_number(self, usernumber):
        browser.element('#userNumber').type(usernumber)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def fill_subjects(self, subj):
        browser.element('#subjectsInput').type(subj).press_enter()

    def upload_picture(self, picture):
        browser.element('#uploadPicture').send_keys(resources.path(picture))

    def fill_current_address(self, address):
        browser.element('[placeholder="Current Address"]').type(address)

    def fill_state(self, name):
        browser.element('#react-select-3-input').type(name).press_enter()

    def fill_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def click_submit(self):
        browser.element('#submit').press_enter()


    def should_registered_user_with(self, full_name, email, gender, phone_number, date_of_birth, subj, hobby, picture, curr_address,
                                    state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subj,
                hobby,
                picture,
                curr_address,
                state_city
            )
        )
