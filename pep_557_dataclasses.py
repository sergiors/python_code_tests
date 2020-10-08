from dataclasses import dataclass


@dataclass
class User:
    name: str
    username: str
    years_old: int


def test_new_user():
    jimi = User('Jimi Hendrix', 'jimi@hendrix.com', 27)
    assert 27 == jimi.years_old
