import json
import requests
from bs4 import BeautifulSoup as bs
import Case_Skins as cls
import web_scrapper as scrapper

URL = 'https://csgostash.com/containers/skin-cases'

if __name__ == '__main__':

    page = requests.get(URL)
    soup = bs(page.content, features='html.parser')

    menu = soup.find('div', {'id': 'navbar-expandable'}).find('ul')
    all_buttons = menu.findAll('li', {'class': 'dropdown'})

    ok = 0
    for button in all_buttons:

        menu = button.findAll('a', {'href': '#'})
        for row in menu:
            if (row.contents[0] == 'Cases'):
                ok = 1
                break

        if ok == 1:
            break

    elem_menu = button.findAll('li')  # accesez lista de elemente din dropdown_menu
    elem_menu_set = set(elem_menu)  # o transform intr-o lista numarabila

    Cases = []
    for case_Link, case_Name in scrapper.extract_data(elem_menu_set):
        ObjCase = cls.Case()
        ObjCase.case_name = case_Name
        ObjCase.link = case_Link
        scrapper.extract_skin_from(ObjCase.link, ObjCase)
        Cases.append(ObjCase)
