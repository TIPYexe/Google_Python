import json
import requests
from bs4 import BeautifulSoup as bs
import Case_Skins as cls
import web_scrapper as scrapper
import dmarket_api as api

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

    print("Gata extractia din meniu")

    Cases = []
    for case_Link, case_Name in scrapper.extract_data(elem_menu_set):
        ObjCase = cls.Case()
        ObjCase.name = case_Name
        ObjCase.link = case_Link
        scrapper.extract_skin_from(ObjCase.link, ObjCase)
        Cases.append(ObjCase)

    print("Gata extractia din cutii")

    # Lista de cutii si procentul pe care sa nu il depaseasca un skin
    # (daca skin-ul valoreaza 10$ si cineva se gaseste sa il vanda cu un pret iesit din comun rau de tot, gen 20$
    # sa nu il luam in calcul)
    api.insert_offer_to_DB(Cases, 10)

    #'''
    for case in set(Cases):
        print("Case Name: " + case.name)
        print("Link: " + case.link)
        for skin in case.Skins:
            print("Weapon: " + skin.weapon + " | Skin: " + skin.name)
            print("FN " + skin.extra['FN'])
            print("FT " + skin.extra['FT'])
            print("SFN " + skin.extra['SFN'])
        print()
    #'''

