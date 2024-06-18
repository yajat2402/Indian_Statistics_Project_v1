import bs4
import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def population():
    url = 'https://www.worldometers.info/world-population/india-population/'

    # Use a headless WebDriver to load the page
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        # Wait for the real data to load (the "retrieving data..." message)
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[id="example"]'))
        )

        # Once the "retrieving data..." message is gone, extract the population data
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        population = soup.find('div', {'class': 'maincounter-number'}).find('span').text
        return population
    finally:
        driver.quit()

while True:
    current_population = population()
    # if current_population is not None:
    #     print('The current population:', current_population)
    current_population = str(current_population)
    current_population = current_population.replace(',','')
    current_population = int(current_population)
    data = {'2023': current_population}
    years = list(data.keys())
    pop = list(data.values())

    # fig = plt.figure(figsize = (10,5))
    plt.bar(years, pop)
 
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Comparison of population in different years")
    plt.show()
    time.sleep(1)
