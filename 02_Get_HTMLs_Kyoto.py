# Second Stage
# Main goal: create a html file out of each one of the articles, with the urls stored in 'URLS_Kyodo.csv'

# Author: Eduardo Pacheco Ardon - 24.5.2022

import requests
import pandas as pd
from bs4 import BeautifulSoup

# print(os.getcwd())

# Importing the Kyoto_URLS.csv file
urls = pd.read_csv("/home/student/Cloud/Owncloud/Institution/SyncVM/CIP_F22/Pycharm/CIP_Project/URLS_Kyodo.csv")
print(urls.head())
print(len(urls))

# Iterating over each url, getting the html content and making a BeautifulSoup object out of it
for idx in range(len(urls)):
    url = urls.iloc[idx, 1]
    print(url)
    html_raw = requests.get(url)
    soup = BeautifulSoup(html_raw.content, 'html.parser')
    html_page = soup.prettify()
    print("*" * 50)

    # creating an individual file for each html with the variable 'html_page'
    file_path = "/home/student/Cloud/Owncloud/Institution/SyncVM/CIP_F22/Pycharm/CIP_Project/html_demo/" \
                + url.split("/")[-1] + ".html"
    file = open(file_path, "w+")
    file.write(html_page)
    # file.write(f'HTML_file.{idx}')        # this line of code was used initially to name the html files before the
    # blocking, but it got replaced, as the name was not descriptive enough.
file.close()
