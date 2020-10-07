"""
    https://docs.python.org/3.8/glossary.html#term-parameter
"""

import pytest


def foo(a, /, b, c, *, d):
    return a, b, c, d


def buzz(a, /, *, b, c, d):
    return a, b, c, d


def test_okey():
    assert (1, 2, 3, 4) == foo(1, 2, 3, d=4)
    assert (1, 2, 3, 4) == foo(1, b=2, c=3, d=4)
    assert (1, 2, 3, 4) == foo(1, 2, 3, d=4)
    assert (1, 2, 3, 4) == buzz(1, b=2, c=3, d=4)


def test_wrong():
    with pytest.raises(TypeError) as excinfo:
        foo(a=1, b=2, c=3, d=4)

    assert "foo() got some positional-only arguments " \
           "passed as keyword arguments: 'a'" in str(excinfo.value)
