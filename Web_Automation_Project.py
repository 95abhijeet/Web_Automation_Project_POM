# https://testautomationpractice.blogspot.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


# --- SETUP ---
chrome_driver_path = r'D:\Projects\Automation Project\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# --- OPEN WEBSITE ---
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)


# --- SCROLL TO FORM ---
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

# --- FILL TEXT FIELDS ---
driver.find_element(By.ID, "name").send_keys("Abhijeet Singh")
driver.find_element(By.ID, "email").send_keys("abhijeet@example.com")
driver.find_element(By.ID, "phone").send_keys("1234567890")

# --- SELECT RADIO BUTTON ---
gender_male = driver.find_element(By.ID, "male")  # Male radio button
gender_male.click()

# --- SELECT CHECKBOXES ---
driver.find_element(By.ID, "sunday").click()  # Example checkbox
driver.find_element(By.ID, "wednesday").click()  # Another checkbox

# --- SELECT DROPDOWN OPTION ---
dropdown_element = driver.find_element(By.ID, "country")
select = Select(dropdown_element)
select.select_by_visible_text("India")  # Select country

# --- SELECT DATE PICKER1 ---
driver.find_element(By.ID, "start-date").send_keys("2025/01/10")

# --- SELECT DATE PICKER2 ---
driver.find_element(By.ID, "end-date").send_keys("2025/10/10")

# --- CLICK BUTTON TO SUBMIT ---
button = driver.find_element(By.CSS_SELECTOR, "button.submit-btn")
driver.execute_script("arguments[0].click()", button)

time.sleep(4)

# --- HANDLE ALERT (if any) ---
try:
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.accept()
except:
    print("No alert appeared.")

# --- TAKE SCREENSHOT ---
driver.save_screenshot("automation_practice_result.png")

# --- FINISH ---
print("Automation script executed successfully!")
driver.quit()