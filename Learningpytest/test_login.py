import pytest
def test_method1():
    a=2
    b=3
    print("addition")
    assert a==3
@pytest.mark.sanity
def test_method2():
    name='selenium'
    title="selenium webdriver"
    assert name in title,"test failed"
def testmethod3():
    print("login in application")
@pytest.mark.skip
def test_method4():
    assert True
