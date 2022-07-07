import requests as rq
from gne import GeneralNewsExtractor

def extract_news(url):
    if ("https" or "http") in url:
        data = rq.get(url)
    else:
        data = rq.get("https://" + url)

    return extract_html(data.text)

def extract_html(html):

    extractor = GeneralNewsExtractor()
    result = extractor.extract(html)
    return result