import pytest


def test_method1(add):
    b = 2
    print("this is testmethod1")
    assert (add ==b)

# @pytest.mark.xfail
def test_method2(add):
    a=2
    print("this is testmethod2")
    assert (a!=add)

@pytest.mark.parametrize("num, output",[(1,1),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output