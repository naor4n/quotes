import random
from search_quote import fetch_quote


def generate_index(len):
    """generates a random even number that is used as index to get a random quote"""

    max = int(len/2)
    index = random.randint(0,max)*2

    return index


def quote(author):
    """calls function fetch_quotes to scrape all quotes and their authors from goodreads. calls generate_index to choose a quote randomly."""

    quotes = fetch_quote(author)
    leng = len(quotes)
    index = generate_index(leng)

    random_quote = quotes[index] + "\n\n" + quotes[index + 1]

    return random_quote
    


random_quote = quote("Natsume Soseki")
print(random_quote)
