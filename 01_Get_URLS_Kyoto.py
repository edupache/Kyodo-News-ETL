# First Stage
# Main goal: To collect all articles URLs from https://english.kyodonews.net/news/ and save them in a csv file.
# In this first stage I am scrapping just the extract of html code, where the url link is located,
# these urls will be stored in a csv file named 'URLS_Kyoto.csv'.

# Author: Eduardo Pacheco Ardon - 24.5.2022

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# setting up the webdriver
driver = webdriver.Chrome('C:/Users/eduar/AppData/Local/Programs/Python/Python310/Scripts')
# url = "https://english.kyodonews.net/news/"
url = 'https://tass.com/'
driver.get(url)

# Scrolling down until the end of the page gets reached, by comparing the page height before and after scrolling down.
old_height = 0
height = 1
while old_height < height:
    old_height = height
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # Masterpiece of code to scroll down ;)
    time.sleep(5)
    height = driver.execute_script("return document.body.scrollHeight")      # One way to measure the height of the page
    print(height)
    if old_height == height:
        print("The end of the page has been reached.\n", "Final page height: ", height)
        break

# saving the element <articles> extract in a list
article_list = driver.find_elements(By.TAG_NAME, "article")
print(len(article_list))
print(article_list)


# finding the url link for each article and storing it in the 'urls' list
urls = []
for article in article_list:
    element = article.find_element(By.TAG_NAME, "a")
    urls.append(element.get_attribute("href"))

# saving the list of urls as a DataFrame and then as a csv file

# df = pd.DataFrame({"url": urls})
# df.to_csv("URLS_Kyodo.csv")

df2 = pd.DataFrame({"url": urls})
df2.to_csv("URLS_TSS.csv")
driver.close()
