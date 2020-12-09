import json
import requests
from bs4 import BeautifulSoup as bs

import web_scrapper as scrapper

URL = 'https://csgostash.com/containers/skin-cases'

if __name__ == '__main__':
    page = requests.get(URL)
    soup = bs(page.content, features='html.parser')

    menu = soup.findAll('a', {'href':'#'})
    #returenaza toate butoanele din meniu, care au un dropdown menu

    dropdown_menu = menu.find('Cases')
    print(dropdown_menu)


