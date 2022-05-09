import pytest


@pytest.fixture(scope="package",autouse=True)
def setup():
    print("launch browser")
    print("login ")
    print("browse product")
    yield
    print("logoff")
    print("close browser")