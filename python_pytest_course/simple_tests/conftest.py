import pytest


@pytest.fixture(autouse=True)
def set_up(browser):
    if browser == "chrome":
        print("Launch Chrome")
    elif browser == "firefox":
        print("Launch FireFox")
    else:
        print("Provide valid browser")
    print("Login")
    yield
    print("Logoff")
    print("Close browser")


@pytest.fixture(params=["a", "b"])
def demo_fixture(request):
    print(request.param)


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption("--browser")
