import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
#from connect import connection

def websiteFansale(url):
    print('a')
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    script = ''' return document.getElementsByClassName('btn btn-alternative btn-sm btn-stepper-right js-tracking js-stepper-more disabled')'''
    text = driver.execute_script(script)
    xn = driver.execute_script('''return document.getElementsByClassName('btn btn-alternative btn-sm btn-stepper-right js-tracking js-stepper-more')''')
    print(xn)
    print(text)
    return text
