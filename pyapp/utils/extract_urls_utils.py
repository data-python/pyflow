import requests as rq
from bs4 import BeautifulSoup

def extract_url(url):
    if ("https" or "http") in url:
        data = rq.get(url)
    else:
        data = rq.get("https://" + url)

    # print(data)
    soup = BeautifulSoup(data.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        if ("javascript:void(0)" or "javascript:;") in link.get("href"):
            continue
        if '/' == link.get("href"):
            continue
        if '#' == link.get("href"):
            continue
        links.append(link.get("href"))

    return links