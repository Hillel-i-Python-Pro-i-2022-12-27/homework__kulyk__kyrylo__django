from collections.abc import Iterator
from random import randint
from typing import NamedTuple
from django.utils.crypto import get_random_string


from faker import Faker


class User(NamedTuple):
    nickname: str
    email: str
    psw: str

    def __str__(self):
        return f"{self.nickname} {self.email} {self.psw}"

    __repr__ = __str__


fake = Faker()


def generate_user() -> User:
    fake_nickname = fake.unique.user_name()
    password = get_random_string(randint(6, 10))
    domain = fake.domain_name()
    return User(nickname=fake_nickname, email=f"{fake_nickname}.{randint(10, 9999)}@{domain}", psw=password)


def generate_users(amount: int = 10) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
