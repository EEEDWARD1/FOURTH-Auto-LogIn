from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
from shift import Shift

class FourthAutomation:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = "https://api.fourth.com/myschedules/"
        self.driver = webdriver.Firefox()
        self.list_of_shifts = []

    def open_website(self):
        self.driver.get(self.url)
    
    def login(self):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'j_id0:j_id2:j_id15:username'))
            )
        except TimeoutException:
            raise Exception("Login page did not load within the expected time.")
        
        try:
            self.driver.find_element(By.ID, 'j_id0:j_id2:j_id15:username').send_keys(self.username)
            self.driver.find_element(By.NAME, 'j_id0:j_id2:j_id15:j_id24').send_keys(self.password)
            self.driver.find_element(By.ID, 'j_id0:j_id2:j_id15:submit').click()
        except NoSuchElementException as e:
            raise Exception(f"Error locating login elements: {e}")

    def extract_shifts(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'shift-group-item__content-area.layout-row'))
            )
            print("Logged in successfully")
        except TimeoutException:
            raise Exception("Shift items did not load within the expected time.")

        print("trying shifts")
        try:
            shift_list_items = self.driver.find_elements(By.CLASS_NAME, "shift-group-item__content-area.layout-row")

            for item in shift_list_items:
                # Get date
                date = item.get_attribute("id")
                # Get role
                role = item.find_element(By.CLASS_NAME, "shift-item__role").text

                # Get start time
                start_time = item.find_element(By.XPATH, ".//div[contains(@class, 'flex-45 layout-row layout-align-start-center')]//span[@class='time__hours']").text

                # Get end time
                end_time = item.find_element(By.XPATH, ".//div[contains(@class, 'flex-45 layout-row layout-align-end-center')]//span[@class='time__hours']").text

                shift = Shift(date, role, start_time, end_time)
                self.list_of_shifts.append(shift)
            print("Shifts extracted successfully")
        except NoSuchElementException as e:
            raise Exception(f"Error extracting shift details: {e}")


    
    def close_browser(self):
        self.driver.quit()
    
    def get_shifts(self):
        return self.list_of_shifts

    def run(self):
        try:
            self.open_website()
            self.login()
            self.extract_shifts()
            self.close_browser()
        except WebDriverException as e:
            print(f"An error occurred: {e}")