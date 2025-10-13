from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage



class FormPage(BasePage):
  
    #  LOCATORS
    name_field = (By.ID, "name")
    email_field = (By.ID, "email")
    phone_field = (By.XPATH, "//input[@id= 'phone']")
    gender_field = (By.ID, "male")
    day_field_checkbox = (By.ID, "sunday")
    day_field2_checkbox = (By.ID, "wednesday")
    country_dropdown = (By.ID, "country")
    start_date = (By.ID, "start-date")
    end_date = (By.ID, "end-date")
    submit_button = (By.CSS_SELECTOR, "button.submit-btn")

    # ACTIONS
    def fill_form(self, data):
        self.scroll(300)
        self.type(self.name_field, data["name"])
        self.type(self.email_field, data["email"])
        self.type(self.phone_field, data["phone"])
        self.click(self.gender_field)
        self.click(self.day_field_checkbox)
        self.click(self.day_field2_checkbox)
        dropdown = self.find(self.country_dropdown)
        self.select_dropdown(dropdown, data ["country"])
        self.type(self.start_date, data["start_date"])
        self.type(self.end_date, data["end_date"])
        
    def submit_form(self):
        self.click(self.submit_button)
