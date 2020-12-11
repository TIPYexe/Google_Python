import json
import requests
from bs4 import BeautifulSoup as bs

import web_scrapper as scrapper

URL = 'https://csgostash.com/containers/skin-cases'

if __name__ == '__main__':

    page = requests.get(URL)
    soup = bs(page.content, features='html.parser')

    menu = soup.find('div', {'id':'navbar-expandable'}).find('ul')
    all_buttons = menu.findAll('li', {'class':'dropdown'})
    ok = 0
    for buton in all_buttons:

        menu = buton.findAll('a', {'href':'#'})
        for row in menu:
            if(row.contents[0] == 'Cases'):
                ok = 1
                break

        if ok == 1:
            break

    elem_menu = buton.findAll('li')
    elem_menu_set = set(elem_menu)

    cases_name = set(map(scrapper.extract_cases, elem_menu_set))

    for name in cases_name:
       print(name)

