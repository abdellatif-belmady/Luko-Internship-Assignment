import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class CreditCardTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # navigate to the sign-in page
        self.driver.get("https://devnoscope.luko.eu/my-account/sign-in?lang=en")

        # give some time for the page to fully load
        time.sleep(5)

        # cookies_button.click()
        cookies_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[3]/button[2]")
        cookies_button.click()

    def test_add_credit_card(self):
        # give some time for the page to fully load
        time.sleep(6)

        # Login to the system
        username = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section/div/div[2]/form/div[1]/div[1]/div/input")
        password = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section/div/div[2]/form/div[1]/div[2]/div/input")
        username.send_keys("qa-user@getluko.com")
        password.send_keys("Faxs9YH5$yR#Rsag")
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section/div/div[2]/form/div[2]/button/span")
        login_button.click()

        # Find the navigation menu
        nav_menu = self.driver.find_elements(By.CSS_SELECTOR, "#side-menu-nav")
        # Iterate over the menu items and click on the "Payment methods" item
        for item in nav_menu:
            if item.text == "Payment methods":
                item.click()
                break  # Exit the loop once we've clicked on the desired item

        # Navigate to the add credit card page
        add_card_button = self.driver.find_elements(By.CSS_SELECTOR, "#header-slot-content > button")

        # Iterate over the menu items and click on the "Add payment method" item
        for item in add_card_button:
            if item.text == "Add payment method":
                item.click()
                break  # Exit the loop once we've clicked on the desired item

        # add_card_button.click()
        card_menu = self.driver.find_elements(By.CSS_SELECTOR, "#choice-card")

        # Iterate over the menu items and click on the "Credit card" item
        for item in card_menu:
            if item.text == "Credit card":
                item.click()
                break  # Exit the loop once we've clicked on the desired item

        # Enter credit card details
        card_number = self.driver.find_element(By.XPATH, '/html/body/div/form/span[2]/div/div[2]/span/input')
        card_number.send_keys("1234567890123456")
        expiration_date = self.driver.find_element(By.XPATH, "/html/body/div/form/span[2]/span/input")
        expiration_date.send_keys("1225")
        cvc_code = self.driver.find_element(By.XPATH, "/html/body/div/form/span[2]/span/input")
        cvc_code.send_keys("123")
        authorize_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div/div[3]/div")
        authorize_button.click()

        # Submit the form
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/button")
        submit_button.click()

        # Verify that the credit card was added
        # success_message = self.driver.find_element_by_css_selector(".alert-success")
        # self.assertEqual(success_message.text, "Credit card added successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
