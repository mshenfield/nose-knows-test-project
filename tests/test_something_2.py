from modules.module_2 import add_things


class TestSomething(object):
    def test_something(self):
        assert add_things() == 4
