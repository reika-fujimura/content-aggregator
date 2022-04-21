import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.bbc.com/news/world")
soup = BeautifulSoup(r.content, 'html5lib')

# newsDivs = soup.findAll("div", {"class": "gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text"})
newsDivs = soup.findAll("div", {"class": "gs-c-promo-heading__title"})

print(newsDivs)

