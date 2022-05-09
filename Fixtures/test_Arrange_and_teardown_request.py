import pytest
@pytest.fixture()
def setup():           #Arrange
    print("launch browser")
    print("login")
    print("browse product")
    yield
    print("logoff")
    print("close browser")

def testadditem(setup):             #requesting fixture
    print("add item successfully")
def testremoveitem(setup):
    print("item removedsuccessfully")