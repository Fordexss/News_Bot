import requests
from bs4 import BeautifulSoup

site_link = "https://www.pravda.com.ua"

r = requests.get(url=site_link + "/news", verify=True)
soup = BeautifulSoup(r.content, "html.parser")

db_of_news = {
        "Економічні новини": [], # [{header, link, body_text}, {header, link, body_text}, {header, link, body_text}, ...]
        "Політичні новини": [],
        "Cуспільні новини": [],
        "Міжнародні новини": [],
    }

def parse_body_text(soup_news: BeautifulSoup, selector: str):
    body_text_list = []
    for p in soup_news.select(selector):
        body_text_list.append(f"{p.text.strip()}\n")
    return " ".join(body_text_list)

for news in soup.select(".article_header > a"):
    news_text = news.text.strip()
    news_href = news.get("href", "") 
    news_link = site_link + news_href if "http" not in news_href else news_href 

    r_news = requests.get(url=news_link, verify=True)
    soup_news = BeautifulSoup(r_news.content, "html.parser")
 
    category = ""
    if "www.pravda" in news_link:
        body_text = parse_body_text(soup_news, ".post_text > p")
        category = "Політичні новини"
    elif "www.epravda" in news_link or "www.eurointegration" in news_link:
        body_text = parse_body_text(soup_news, ".post__text > p")
        category = "Економічні новини" if "epravda" in news_link else "Міжнародні новини"
    elif "life.pravda" in news_link:
        body_text = parse_body_text(soup_news, ".article > p")
        category = "Cуспільні новини"


    db_of_news[category].append({
        "header": news_text, 
        "link": news_link,
        "body_text": body_text,
    })
