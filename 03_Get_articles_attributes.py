# Third Stage
# Main goal: Here I have defined a function to obtain each one of the articles attributes. First I create a variable
# with all the paths to where the html files are located, extract the html content, make it a Beautiful Soup object
# and pass it through all the attributes functions. The output of the functions are appended and stored as a dictionary,
# then as a DataFrame and finally as a csv file.

# Author: Eduardo Pacheco Ardon - 24.5.2022

import glob
from bs4 import BeautifulSoup as bs
import pandas as pd

# Create a list with the paths to the html files contained in folder 'htmls'
path_to_data = "htmls/"
articles_html_path = [f for f in glob.glob(path_to_data + "*.html", recursive=True)]
print(type(articles_html_path))


# Defining a function to extract each one of the article's attributes


def get_title(article_soup):
    try:
        title_tem = article_soup.find("title").get_text()
        title_tem = title_tem.replace("\n   ", "")          # Some cleaning up to get just the title
        return title_tem.replace("\n  ", "")
    except:
        return ""


def get_key_words(article_soup):
    try:
        return article_soup.find("meta", attrs={'name': 'keywords'}).attrs["content"].split(",")
    except:
        return ""


def get_description(article_soup):
    try:
        # return article_soup.find('div.main h1', first=True).text
        return article_soup.find("meta", attrs={'name': 'description'}).attrs["content"]
    except:
        return ""


def get_date_time_channels(article_soup):
    try:
        return article_soup.find("div", attrs={'class': 'wrapper'}).find("div", attrs={'class': 'main'}). \
            find("p", attrs={'class': 'credit'}).text

    except:
        return ""


def get_author(article_soup):
    try:
        return article_soup.find("meta", attrs={'name': 'author'}).attrs["content"]

    except:
        return []


def get_paragraph(article_soup):
    try:
        return article_soup.find("div", attrs={'class': 'article-body'}).find_all("p")
    except:
        return []


def get_url(article_soup):
    try:
        return article_soup.find("meta", attrs={'property': 'og:url'}).attrs["content"]

    except:
        return []


# Iterating over the html file paths, get the content, make it a BeatifulSoup object and pass it through  the
# attributes functions:

articles = []
for idx, article in enumerate(articles_html_path):
    if idx >= 8600:
        break
    print(idx, article)                 # I print the index and file name to visually see how it runs

    with open(article) as data:
        data = data.read()
        soup = bs(data, 'lxml')
        title = get_title(soup)
        keywords = get_key_words(soup)
        description = get_description(soup)
        time_channel = get_date_time_channels(soup)
        author = get_author(soup)
        paragraph = get_paragraph(soup)
        url = get_url(soup)

        articles.append(
            {"title": title, "keywords": keywords, "description": description, "time_channel": time_channel,
             "author": author,
             "paragraph": paragraph, "url": url})

# Creating a dataframe to store it in a csv file
df = pd.DataFrame(articles)
print(df.head(5))
df.to_csv("article_features.csv")
