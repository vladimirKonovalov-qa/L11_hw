import datetime
from data.user import User, Hobbies
from models.pages.registration_page import RegistrationPage


def test_registration():
    vasya = User('Vasya', 'Zadov', 'ZadovVasya@pochta.org', 'Male', '9876567456', datetime.date(1974, 2, 3), 'Maths',
                 Hobbies.Reading, '230018.jpg', 'Boslhaya st, 19', 'NCR', 'Gurgaon')
    registration_page = RegistrationPage()

    registration_page.open_started_page()
    registration_page.register(vasya)
    registration_page.should_have_registered(vasya)


