from bs4 import BeautifulSoup
from .connect import connection
import re


def filterNumber(number):
    num = ''
    for n in str(number).split('.'):
        num = num+n
    return num

def websiteklein(url):
    response = 0
    new_ticket_name = []
    last_response = 0
    number_of_ticket = 0

    try:
        response = connection(url)
    except TimeoutError:
        print('timeout')

    if response['status_code'] == 200:
        soup = BeautifulSoup(response['text'], "html.parser")
        list_ticket_name = soup.find_all("a", class_="ellipsis")
        count_in_text = soup.find_all("span",class_="breadcrump-summary")[0].text
        number_of_ticket = re.findall(r'-?\d+(?:,\d{3})*(?:\.\d+)?',count_in_text)
        for n in list_ticket_name:
            new_ticket_name.append(n.text)

    page_num = filterNumber(number_of_ticket[2])

    return [page_num, new_ticket_name]

#good to go
