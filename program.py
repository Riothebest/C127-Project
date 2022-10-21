from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

Start_Url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/Dhody/Documents/Rio/Whitehatjr/WH Jr Projects/C127/chromedriver")
browser.get(Start_Url)
time.sleep(10)

def scrape():
    headers = ["name","mass","distance","radius"]
    planet_data = []
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for ul_tags in soup.find_all("ul",attrs = {"class","star"}):
        li_tags = ul_tags.find_all("li")
        temp_list = []
        for index,li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
    with open("scrapped.csv","w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)


scrape()