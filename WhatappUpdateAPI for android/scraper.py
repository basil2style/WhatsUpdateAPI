__author__ = 'Basil T Alias'

from bs4 import BeautifulSoup as bs
from urllib2 import urlopen


def main():
    url = "http://www.whatsapp.com/android/"
    soup = bs(urlopen(url))
    alink  = soup.findAll("a", { "class" : "button" })
    for a in alink:
        link = a['href']
    version = soup.find("p").get_text()
    ver =   version.split()[1]
    return [link,ver]

if __name__ == "__main__":
    main()

