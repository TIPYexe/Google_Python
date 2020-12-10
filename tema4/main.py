import json
import requests
from bs4 import BeautifulSoup as bs

#import web_scrapper as scrapper

URL = 'https://csgostash.com/containers/skin-cases'

if __name__ == '__main__':
    page = requests.get(URL)
    soup = bs(page.content, features='html.parser')

    ul_menu = soup.find('div', {'id':'navbar-expandable'}).find('ul')
    ul_menu2 = ul_menu.findAll('li', {'class':'dropdown'})

    ok = 0
    for buton in ul_menu2:

        menu = buton.findAll('a', {'href':'#'})
        for row in menu:
            if(row.contents[0] == 'Cases'):
                ok = 1
                break

        if ok == 1:
            break

    elem_menu = buton.findAll('li')

    for name_case in elem_menu:
        sub_cat = name_case.find('a')
        print('SubCat: ', sub_cat, '\n')
