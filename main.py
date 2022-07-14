#
# import requests
# r=requests.get("https://steamdb.info/graph/")
# print(r.text)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
import csv

# open the file in the write mode


driver = webdriver.Firefox(r"C:\Users\174239\PycharmProjects\SteamDBScrapper")
driver.get("https://steamdb.info/graph/?sort=peak")
lines = driver.find_elements(By.CSS_SELECTOR, "tr")
headers = lines[0].find_elements(By.CSS_SELECTOR, "th")

with open('All time Most Played Games on Steam.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    header_data = [headers[0].text, headers[2].text, headers[3].text, headers[4].text, headers[5].text]
    # write a row to the csv file
    writer.writerow(header_data)

    for line in lines[1:]:
        items = line.find_elements(By.CSS_SELECTOR, "td")
        data = [items[0].text, items[2].text, items[3].text, items[4].text, items[5].text]
        writer.writerow(data)
