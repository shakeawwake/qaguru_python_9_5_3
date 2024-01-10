from dataclasses import dataclass


@dataclass
class User:
    name: str
    lastname: str
    email: str
    gender: str
    phone: str
    birthday_year: str
    birthday_month: str
    birthday_day: str
    hobby: str
    subject: str
    picture: str
    address: str
    state: str
    city: str


user = User(name='TestName',
            lastname='TestLastName',
            email='test@user.test',
            gender='Female',
            phone='8916506361',
            birthday_year='1994',
            birthday_month='July',
            birthday_day='03',
            hobby='Sports',
            subject='English',
            picture='logo.png',
            address='TestAdress',
            state='NCR',
            city='Noida'
            )
