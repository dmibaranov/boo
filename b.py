import re
import sys

try:
    assert sys.version_info >= (3, 7)
except AssertionError:
    print('Cannot boo')

__all__ = []


def _get_oos(string):
    return re.sub('[^oO]', '', string)


class Boo:
    def __init__(self, oos=2):
        assert isinstance(oos, int)
        assert oos >= 2
        self.oos = oos

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'b{"o" * self.oos}'

    def __enter__(self):
        print(self)

    def __exit__(self, type, value, tb):
        print(self)

    def __getattr__(self, attr):
        oos = len(_get_oos(attr))
        if oos and oos == len(attr):
            return Boo(self.oos + oos)
        else:
            raise AttributeError(f"{self!r} has no attribute {attr!r}")


def __getattr__(name):
    oos = len(_get_oos(name))
    if oos and oos == len(name):
        return Boo(oos)
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return __all__
