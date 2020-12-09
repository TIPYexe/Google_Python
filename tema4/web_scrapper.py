from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def click_sequence():
    driver = webdriver.Firefox()
    driver.get("https://csgostash.com/")
    elem = driver.find_element_by_xpath('//*[@id="navbar-expandable"]/ul/li[7]/a')
    #XPath of the button

    #button = driver.find_element_by_id('Cases')
    elem.click()
    print(elem.get_property("href"))
    driver.close()
