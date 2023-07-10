import pytest


@pytest.mark.regression
def test_login(demo_fixture):
    print("Login successful!")


def test_logoff():
    print("Logoff successful")


@pytest.mark.xfail
def test_calculation():
    assert 2 + 2 == 4
