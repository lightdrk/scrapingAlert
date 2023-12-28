import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
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
    html = driver.page_source
    script = '''return document.getElementsByClassName('btn btn-alternative btn-sm btn-stepper-right js-tracking js-stepper-more disabled')'''
    text = driver.execute_script(script)
    print(text)
    return text

