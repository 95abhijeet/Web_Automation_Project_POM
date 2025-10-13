from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)
    
    def select_dropdown(self, select_obj, text):
        Select(select_obj).select_by_visible_text(text)

    def scroll(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def take_screenshot(self):
        screenshot_dir = 'D:\\Projects\\Web_Automation_Project_POM\\screenshots'
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"automation_practice-screenshot_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        self.driver.save_screenshot(screenshot_path)
