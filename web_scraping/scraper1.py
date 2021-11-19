from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as err:
        return None

    try:
        bs = BeautifulSoup(html.read(), "html5lib")
        title = bs.body.h1
    except AttributeError as err:
        return None
    return title


URL = 'http://www.pythonscraping.com/pages/page1.html'
title = get_title(URL)

if title is None:
    print("Title could not be found")
else:
    print(title)

