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

    for quoteText in text:
        for element in quoteText:
            if isinstance(element, NavigableString):
                    element = element.replace("\n", "")
                    element = element.replace("―", "")
                    quotes.append(element)     


    while not data.find_all('span', {"class": "next_page disabled"}):
        page_num += 1

        url = "https://www.goodreads.com/quotes/search?commit=Search&page=" + str(page_num) + "&q=" + author + "&utf8=%E2%9C%93"

        page = requests.get(url)
        data = BeautifulSoup(page.text, 'html.parser')
        

        # find the quote itself
        quoteText = data.find_all('div', {"class": "quoteText"})
        for quoteText in text:
            for element in quoteText:
                if isinstance(element, NavigableString):
                        element = element.replace("\n", "")
                        quotes.append(element)     

        # find quote author
        quoteAuthor = data.find_all('div', {"class": "authorOrTitle"})

        # find title
        quoteTitle = data.find_all('div', {"class": "authorOrTitle"})

    for quote in quotes:
         print(quote)




    return quotes


fetch_quote("Natsume Soseki")


