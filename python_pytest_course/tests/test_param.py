import pytest


@pytest.mark.parametrize("a, b, final", [(2, 6, 8), (5, 8, 15), (5, 10, 15)])
def tests_add(a, b, final):
    assert a + b == final
