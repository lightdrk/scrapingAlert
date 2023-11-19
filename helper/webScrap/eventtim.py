import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def filterNumber(number):
    num = ''
    for n in number:
        try:
            if int(n) >= 0:
                num = num + str(n)
        except:
            continue
    return int(num)

def eventtim(driver, url):
    driver.get(url)

    # Wait for the entire page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    try:
        # Wait for the button to be clickable
        add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'add_button_id')))
        # If the button is clickable, click it
        add_button.click()

    except TimeoutException:
        # Handle the timeout exception
        print("Timeout waiting for the button to be clickable.")

    # JavaScript code to disable the button based on conditions
    script = """
        var addButton = document.getElementById('add_button_id');
        var ticketsAvailable = 10;  // Replace with the actual number of available tickets
        var all_tickets_sold = false;  // Replace with the actual condition

        if (ticketsAvailable <= 0 || all_tickets_sold) {
            addButton.disabled = true;
        } else {
            addButton.disabled = false;
        }
    """

    # Execute the JavaScript script
    driver.execute_script(script)

    # Perform additional actions if needed

Create the driver outside the function
driver = webdriver.Chrome()

Call the function with the driver
eventtim(driver, "https://www.eventim.de/event/luciano-seductive-tour-lanxess-arena-17385701/?affiliate=TUG#tab=vip_packages-17489755")

Quit the driver after completing the actions
driver.quit()


