"""module for scraping the quotes from goodreads."""

import requests
from bs4 import BeautifulSoup, NavigableString

def fetch_quote(author):

    page_num = 1
    author = author.replace(" ", "+")
    quotes = []
    
    url = "https://www.goodreads.com/quotes/search?commit=Search&page=" + str(page_num) + "&q=" + author + "&utf8=%E2%9C%93"

    page = requests.get(url)
    data = BeautifulSoup(page.text, 'html.parser')
    text = data.find_all('div', {"class": "quoteText"})


    for quote_text in text:
        for element in quote_text:
            if isinstance(element, NavigableString):
                    element = element.replace("\n", "")
                    element = element.replace("―", "")
                    quotes.append(element)

        quote_author = quote_text.find(class_="authorOrTitle").text
        quote_author = quote_author.replace(",", "")
        quote_author = quote_author.strip()
        quotes.append(quote_author)


    while not data.find_all('span', {"class": "next_page disabled"}):
        page_num += 1

        url = "https://www.goodreads.com/quotes/search?commit=Search&page=" + str(page_num) + "&q=" + author + "&utf8=%E2%9C%93"

        page = requests.get(url)
        data = BeautifulSoup(page.text, 'html.parser')

        # find the quote itself
        text = data.find_all('div', {"class": "quoteText"})
        
        for quote_text in text:
            for element in quote_text:
                if isinstance(element, NavigableString):
                        element = element.replace("\n", "")
                        element = element.replace("―", "")
                        quotes.append(element)
                
            quote_author = quote_text.find(class_="authorOrTitle").text
            quote_author = quote_author.replace(",", "")
            quote_author = quote_author.strip()
            quotes.append(quote_author)

    quotes = [ele for ele in quotes  if ele.strip()]
    
    for quote in quotes:
         print(quote)


fetch_quote("Natsume Soseki")


