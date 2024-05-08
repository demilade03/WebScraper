import requests
from bs4 import BeautifulSoup


def main():
    user_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
    soup = get_web_response(user_url)
    article_tag = soup.find_all("article")

    for tag in article_tag:
        span_tag = tag.span
        if "data-test" not in span_tag.attrs.keys():
            continue
        article_link = user_url + tag.a["href"]
        article_soup = get_web_response(article_link)
        article_content = article_soup.find_all("p")

        for article_tag in article_content:
            print(f"\n{article_tag}")
            print("-------------------------------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------------------------------\n")


def get_web_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        return soup
    return response.status_code


if __name__ == "__main__":
    main()
