import pytest
@pytest.mark.xfail
def test_method1():
    a=2
    b=3
    print("addition")
    assert a==3
@pytest.mark.sanity
def test_method2():
    a=3
    b=3
    assert a==3
