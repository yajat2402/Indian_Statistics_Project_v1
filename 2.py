from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.worldometers.info/world-population/india-population/'

def get_population_count(wait,link):
    driver.get(link)
    while True:
        item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='india-population']"))).text
        if "retrieving data" not in item:
            break
    return item

if __name__ == '__main__':
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver,5)
        print(get_population_count(wait,link))