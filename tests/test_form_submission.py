# https://testautomationpractice.blogspot.com/

import pytest
from pages.form_page import FormPage

def test_form_submission(driver, config):
    page = FormPage(driver)
    page.open(config["url"])
    page.fill_form(config["form_data"])
    page.submit_form()
    page.take_screenshot()


    # --- ASSERTION ---
    assert "Automation Testing Practice" in driver.title, "Page title is incorrect"

    