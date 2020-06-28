import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
@pytest.fixture
def sample_fixture():
    a=35
    b=36
    print("Inside Fixture")
    return [a,b]

@pytest.fixture
def browser_launch():

    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver.get("http://www.google.com")

