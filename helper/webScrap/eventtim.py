import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def filterNumber(number):
    num = ''
    for n in number:
        try:
            if int(n) >= 0:
                num = num + str(n)
        except:
            continue
    return int(num)

def eventtim(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    script = "return document.getElementsByClassName('your-button-class').length > 0;"
    buttons_exist = driver.execute_script(script)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    list_ticket_name = soup.find_all("div", class_="event-listing-city theme-text-color")
    new_ticket_name = []
    for n in list_ticket_name:
        new_ticket_name.append(n.text)
    number = filterNumber(html)  # Fix: Use 'html' instead of 'text'

    return [number, new_ticket_name]

driver = webdriver.Chrome()
driver.get('url')

# Wait for the button to be present
add_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'add_button_id')))

# JavaScript code to disable the button based on conditions
script = """
var addButton = document.getElementById('add_button_id');
if (ticketsAvailable <= 0) {
    addButton.disabled = true;
} else {
    addButton.disabled = false;
}
"""

# Pass ticketsAvailable and all_tickets_sold values as arguments
driver.execute_script(script, ticketsAvailable=10, all_tickets_sold=False)  # Replace with actual values

driver.quit()

url = "https://www.eventim.de/event/luciano-seductive-tour-lanxess-arena-17385701/?affiliate=TUG#tab=vip_packages-17489755"

