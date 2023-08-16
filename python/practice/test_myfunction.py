import pytest

def my_function(a,b):
    tmp = a[1]
    a[1] = b[1]
    b[1] = tmp

def test_simple():
    x=[1,2]
    y=[3,4]
    my_function(x,y)
    assert [1,4]==x
    assert [3,2]==y
