import math_func
import os
import pytest

@pytest.mark.parametrize ('x,y,result',[(7,3,10),('Hello','world','Helloworld'),(10.5,25.5,36)])
def test_add(x,y,result):
    assert math_func.add(x, y) == result
