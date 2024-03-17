import pytest

@pytest.fixture()
def add():
    a=2
    print("this is fixture")
    return a