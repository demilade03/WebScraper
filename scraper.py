import requests
from bs4 import BeautifulSoup


def main():
    user_url = input("Enter a URL: ")
    soup = get_web_response(user_url)
    for tag in get_tags(soup):
        print(tag)


def get_tags(obj):
    tags = {}
    for tag in obj.find_all():
        if tag.name not in tags:
            tags[tag.name] = 1
        else:
            tags[tag.name] += 1
    return tags


def get_web_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        return soup
    return response.status_code


if __name__ == "__main__":
    main()
