from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
import json

try:
    signInName = ''
    Password = ''

    url = "https://api.fourth.com/myschedules/"

    driver = webdriver.Firefox()
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'j_id0:j_id2:j_id15:username'))
        )
    except TimeoutException:
        raise Exception("Login page did not load within the expected time.")

    try:
        driver.find_element(By.ID, 'j_id0:j_id2:j_id15:username').send_keys(signInName)
        driver.find_element(By.NAME, 'j_id0:j_id2:j_id15:j_id24').send_keys(Password)
        driver.find_element(By.ID, 'j_id0:j_id2:j_id15:submit').click()
    except NoSuchElementException as e:
        raise Exception(f"Error locating login elements: {e}")

    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'shift-group-item__content-area.layout-row'))
        )
        print("Logged in successfully")
    except TimeoutException:
        raise Exception("Shift items did not load within the expected time.")

    try:
        shift_list_items = driver.find_elements(By.CLASS_NAME, "shift-group-item__content-area.layout-row")
        items = []

        for item in shift_list_items:
            # Get date
            date = item.get_attribute("id")
            # Get role
            role = item.find_element(By.CLASS_NAME, "shift-item__role").text

            # Get start time
            start_time = item.find_element(By.XPATH, ".//div[contains(@class, 'flex-45 layout-row layout-align-start-center')]//span[@class='time__hours']").text

            # Get end time
            end_time = item.find_element(By.XPATH, ".//div[contains(@class, 'flex-45 layout-row layout-align-end-center')]//span[@class='time__hours']").text

            print(f"Date: {date}, Role: {role}, Start Time: {start_time}, End Time: {end_time}")
    except NoSuchElementException as e:
        raise Exception(f"Error extracting shift details: {e}")

except WebDriverException as e:
    print(f"WebDriver error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
