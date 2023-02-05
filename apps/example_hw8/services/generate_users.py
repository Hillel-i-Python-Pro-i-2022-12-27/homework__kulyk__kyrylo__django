from collections.abc import Iterator
from random import randint
from typing import NamedTuple
from django.utils.crypto import get_random_string
from faker import Faker


class User(NamedTuple):
    nickname: str
    email: str
    password: str

    def __str__(self):
        return f"{self.nickname} {self.email} {self.password}"

    __repr__ = __str__


fake = Faker()


def generate_user() -> User:
    fake_nickname = f"{fake.unique.user_name()}_{fake.word()}"
    password = get_random_string(randint(6, 10))
    domain = fake.domain_name()
    return User(nickname=fake_nickname, email=f"{fake_nickname}.{randint(10, 999)}@{domain}", password=password)


def generate_users(amount: int = 10) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
