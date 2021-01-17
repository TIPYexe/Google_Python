import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import Case_Skins as cls
from selenium.webdriver.firefox.options import Options

#region Extrag numele cutiilor


def extract_case_link_name(data):
    return (data.find('a').get('href'), data.find('img').get('alt'))


# pastrez doar diviziunile cu date despre cutii
# adica fara datele extrase gresit
def filter_cases(case_text):

    img_stat = case_text.find('img') is not None
    if not img_stat:
        return False

    case_name = case_text.find('img').get('alt')
    except_1 = case_name != 'All Skin Cases'
    except_2 = case_name != 'Souvenir Packages'
    except_3 = case_name != 'Gift Packages'

    if except_1 and except_2 and except_3:
        return True

def extract_data(data):
    data_filtered = set(filter(filter_cases, data))
    return  set(map(extract_case_link_name, data_filtered))

#endregion

def extract_skin_from(URL, ObjCase):
    page = requests.get(URL)
    soup = bs(page.content, features='html.parser')

    case_name = soup.find('h1', {'class': 'margin-top-sm'}).text

    skin_boxes = soup.findAll('div', {'class': 'col-lg-4 col-md-6 col-widen text-center'})


    # nu iau prima fereastra pentru ca este cu cutite, si nu poti face trade cu ele
    for box in skin_boxes[1:]:
        ObjSkin = cls.Skin()

        # extrage numele skinului si al armei, separat
        ObjSkin.weapon = box.find('h3').text.split(" | ")[0]
        ObjSkin.name = box.find('h3').text.split(" | ")[1]
        ObjSkin.rarity = box.find('p', {'class': 'nomargin'}).text.split(' ')[0]
        ObjCase.Skins.append(ObjSkin)
