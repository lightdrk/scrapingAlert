import re
import requests
from bs4 import BeautifulSoup

def filterNumber(number):
    num = ''
    for n in str(number).split('.'):
        num = num+n
    #checks for float inistance if true increases the value to 1+
    value = int(num)/30

    if isinstance(value,float):
        value = int(value) + 1

    return value

def websiteWill(url):
    new_ticket_name = []
    number_of_ticket = 0
    response = 'a'
    last_response = 'a'
    try:
        response = requests.get(url, timeout=5)

    except TimeoutError:
        print('Timeout')


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        cout_in_text = soup.find(id="result-list-title").text
        number_of_ticket = re.findall(r'-?\d+(?:,\d{3})*(?:\.\d+)?',cout_in_text)[0]
    page_num = filterNumber(number_of_ticket)
    url_last_page = f'&page={page_num}&adSeparatorSeen=false'

    try:
        last_response = requests.get(url+url_last_page, timeout=5)
    except TimeoutError:
        print('timeout')
    if last_response.status_code == 200:
        list_soup = BeautifulSoup(last_response.text, 'html.parser')
        for n in list_soup.findAll('h3'):    #class_= "Text-sc-10o2fdq-0 dphSxt"
            new_ticket_name.append(n.text)
    return [number_of_ticket, new_ticket_name]

#good to go
