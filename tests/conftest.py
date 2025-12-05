import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from pathlib import Path
import os

@pytest.fixture(scope = "session")
def config():
    with open ("./config/config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope = "function")
def driver():
    # Use webdriver-manager to download a matching Chromedriver.
    options = Options()
    # In CI we generally want headless mode and some flags to avoid sandbox issues
    if os.environ.get("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
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