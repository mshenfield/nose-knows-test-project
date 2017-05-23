from unittest import TestCase
from modules.module import (
    add_things,
    add_things_things,
)


class TestSomething(TestCase):
    def test_something(self):
        assert add_things() == 2


def test_something():
    assert add_things_things() == 3
