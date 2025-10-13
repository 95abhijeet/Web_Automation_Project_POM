import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope = "session")
def config():
    with open ("./config/config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope = "function")
def driver():
    chrome_driver_path = r'D:\Projects\Web_Automation_Project_POM\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
