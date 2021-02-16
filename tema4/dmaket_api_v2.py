from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pylightxl as xl
import Case_Skins as cls
import save_to_db as save


def search_skin(Cases, driver):
    for case in Cases:
        for skin in case.Skins:

            # initializez toate preturile skinului cu -1
            for i in range(0, 11):
                skin.prices.append(-1)

            inputElement = driver.find_element_by_id('searchInput')
            inputElement.clear()
            inputElement.send_keys(skin.weapon + ' ' + skin.name)
            inputElement.send_keys(Keys.ENTER)

            # Astept sa se incarce pagina (adica sa apara numele skin-ului in prima caseta din tabel)
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[22]/div/div/div[4]/div/div/div[2]/div/table/tbody/tr[1]'), skin.name))

            # fac media preturilor de pe site-uri si o adaug lui skin, la calitatea care trebuie
            for i in range(1, 11):
                try:
                    table_row = driver.find_element_by_xpath(
                        '/html/body/div[22]/div/div/div[4]/div/div/div[2]/div/table/tbody/tr[' + str(
                            i) + ']').text
                    data = table_row.split(' ')

                    # numar cate caractere sar pentru a ajunge la preturi
                    count = 0
                    for index, elem in enumerate(data):
                        if '(' in elem:
                            count = index + 1
                            break

                    plus1 = 0
                    if 'stattrak' in data[0].lower():
                        plus1 += 1

                    # facem media preturilor de pe toate site-urilor
                    sum = 0
                    nr = 0
                    print(skin.name, data[count + 3:count + 10])
                    for info in data[count + 2:count + 10]:
                        if 'N/A' not in info:
                            nr += 1
                            sum += float(info)
                    print(sum, nr)
                    if nr > 0:
                        sum = sum / nr
                    else:
                        sum = -1
                    print(sum)

                    # adaug pretul la CALITATEA care trebuie
                    if '(FN)' in table_row:
                        skin.prices[plus1 * 5 + 0] = sum
                    if '(MW)' in table_row:
                        skin.prices[plus1 * 5 + 1] = sum
                    if '(FT)' in table_row:
                        skin.prices[plus1 * 5 + 2] = sum
                    if '(WW)' in table_row:
                        skin.prices[plus1 * 5 + 3] = sum
                    if '(BS)' in table_row:
                        skin.prices[plus1 * 5 + 4] = sum

                except NoSuchElementException:
                    print(skin.name + ' e mai mic')


# va fi apelata pentru fiecare cutie
def read_xl(db, sheet_name, Cases):
    [roww, coll] = db.ws(sheet_name).size
    data = db.ws(sheet_name).range('A2:N' + str(roww))
    for row in data:
        ObjSkin = cls.Skin()
        ObjSkin.name = row[0]
        ObjSkin.weapon = row[1]
        ObjSkin.rarity = row[2]
        Cases.Skins.append(ObjSkin)


Cases = []
db = xl.readxl('Case_data.xlsx')
sheet_names = db.ws_names

for sheet in sheet_names[1:]:
    ObjCase = cls.Case()
    ObjCase.name = sheet
    read_xl(db, sheet, ObjCase)
    Cases.append(ObjCase)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

driver.get('https://csgo.steamanalyst.com/markets')
time.sleep(13)


search_skin(Cases, driver)

driver.close()

# for case in Cases[:1]:
#     print("Case Name: " + case.name)
#     for skin in case.Skins:
#         print("Weapon: " + skin.weapon + " | Skin: " + skin.name)
#         print(skin.prices)
#     print()

print('-- SAVE DB --')
save.to_xlsx(Cases, 'Case_data_2.xlsx')
