import os

from selene import have, browser, be, command

import test_hw
from data.user import User


class RegistrationPage:
    def open_started_page(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user: User):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').should(be.blank).type(user.last_name)
        browser.element('#userEmail').should(be.blank).type(user.email)
        browser.element(f'[name="gender"][value="{user.gender}"]+label').click()
        browser.element('#userNumber').should(be.blank).type(user.mobile)
        browser.element('#dateOfBirthInput').click().perform(command.js.scroll_into_view)
        browser.element('.react-datepicker__month-select').send_keys(user.date_of_birth.month)
        browser.element('.react-datepicker__year-select').send_keys(user.date_of_birth.year)
        browser.element(f'.react-datepicker__day--00{user.date_of_birth.day}:not(.react-datepicker__day--outside-month)').click()
        browser.element('#subjectsInput').type(user.subjects).press_tab()
        browser.all('[id^=hobbies-checkbox]+[class="form-check-label"]').element_by(
            have.exact_text(user.hobbies.name)).click()
        browser.element('#uploadPicture').send_keys(
            os.path.abspath(os.path.join(os.path.dirname(test_hw.__file__), 'resources/230018.jpg')))
        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()
        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.mobile,
            user.date_of_birth.strftime('%d %B,%Y'),
            user.subjects,
            user.hobbies.name,
            user.picture,
            user.address,
            f'{user.state} {user.city}'
        ))
