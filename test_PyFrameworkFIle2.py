import pytest

@pytest.mark.smoke
def test2_method1(sample_fixture):
    x=25
    y=26
    print("Inside second file ", sample_fixture)
    print("This is test method")
    assert x == y ,"Value does not match"

@pytest.mark.sanity
def test2_method2(sample_fixture):
    x=sample_fixture[0]
    y=sample_fixture[1]
    print("Inside second file ",sample_fixture)
    print("this is test method 2")
    assert x+1==y , "Value fail to match"

@pytest.mark.function
def test_fixtureSample(browser_launch):
    print("This is test fn after fixture")