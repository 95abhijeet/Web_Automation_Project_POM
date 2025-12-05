import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pathlib import Path
import os

@pytest.fixture(scope = "session")
def config():
    with open ("./config/config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope = "function")
def driver():
    #chrome_driver_path = r'D:\Projects\Web_Automation_Project_POM\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    #service = Service(chrome_driver_path)
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_configure(config):
    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    report_name = f"HTML_Report_{timestamp}.html"
    report_path = os.path.join(report_dir, report_name)
    config.option.htmlpath = report_path