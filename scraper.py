import requests
from bs4 import BeautifulSoup


user_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
response = requests.get(user_url, headers={"Accept-Language": "en-US,en;q=0.5"})

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "lxml")
    article_tag = soup.find_all("article")

    for tag in article_tag:
        span_tag = tag.span
        try:
            if span_tag["data-test"]:
                print(f"\n{span_tag.string}")
                print(
                    "===============================================================================================\n")
        except KeyError:
            continue
else:
    print(f"The URL returned {response.status_code}!")
