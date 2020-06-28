import pytest


@pytest.mark.smoke
def test1_method1(sample_fixture):
    x = 25+sample_fixture[0]
    y = 26+sample_fixture[1]
    print(x)
    print(y)
    print("This is test method")
    assert x != y, "Value does not match"


@pytest.mark.sanity
def test1_method2(sample_fixture):
    x = 25
    y = 26
    print(sample_fixture)
    print("this is test method 2")
    assert x+1 == y, "Value fail to match"
