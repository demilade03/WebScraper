import requests
from bs4 import BeautifulSoup


user_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
response = requests.get(user_url, headers={"Accept-Language": "en-US,en;q=0.5"})

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "lxml")
    article_tag = soup.find_all("article")
    article_links = []

    for tag in article_tag:
        span_tag = tag.span
        if "data-test" not in span_tag.attrs.keys():
            continue
        article = requests.get(f"{user_url + tag.a['href']}")
        article_soup = BeautifulSoup(article.content, "lxml")
        article_content = article_soup.find_all("p")

        for article_tag in article_content:
            print(f"\n{article_tag}")
            print("-------------------------------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------------------------------\n")
else:
    print(f"The URL returned {response.status_code}!")
