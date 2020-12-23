import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.firefox.options import Options

#region Extrag numele cutiilor


def extract_case_name(data):
    return data.find('img').get('alt')

def extract_case_link(data):
    return data.find('a').get('href')


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
    #cols = ['Name', 'Link', 'Convert', 'Classified', 'Restricted', 'Mil-Spec']
    data_filtered = set(filter(filter_cases, data))
    cases_names = set(map(extract_case_name, data_filtered))
    cases_links = set(map(extract_case_link, data_filtered))

    return (cases_names, cases_links)

#endregion

def extract_skin_from(URL):
    page = requests.get(URL)
    soup = bs(page.content, features='html.parser')

    case_name = soup.find('h1', {'class': 'margin-top-sm'}).text

    skin_boxes = soup.findAll('div', {'class': 'col-lg-4 col-md-6 col-widen text-center'})

    # nu iau prima fereastra pentru ca este cu cutite, si nu poti face trade cu ele
    for box in skin_boxes[1:]:
        # extrage numele cu tot cu | dar merge bine in motorul de cautare de pe DMarket
        skin_name = box.find('h3').text
        skin_rarity = box.find('p', {'class': 'nomargin'}).text.split(' ')[0]



'''
options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)
driver.get("https://csgostash.com/case/308/Operation-Broken-Fang-Case")

driver.find_element_by_class_name('qc-cmp-button').click()

case_name = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/h1').text

#skin_boxes = driver.findAll('div', {'class':'col-lg-4 col-md-6 col-widen text-center'})
box = driver.find_element_by_class_name('col-lg-4 col-md-6 col-widen text-center')

#for box in skin_boxes:
skin_name = box.find_element_by_css_selector('h3').find_elements_by_css_selector('a').__getattribute__('text')
print(skin_name)
'''

