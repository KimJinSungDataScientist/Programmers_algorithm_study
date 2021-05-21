from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen


driver = webdriver.Chrome(
    executable_path= './chromedriver'
)

url = "https://m.store.musinsa.com/app/menu"
driver.get(url)
action = ActionChains(driver)
print(driver.find_element_by_xpath('//*[@id="tab-category"]/ul/li[1]/ul/li[1]/a').text)
