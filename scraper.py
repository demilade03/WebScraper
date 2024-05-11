import requests
from bs4 import BeautifulSoup


def main():
    user_url = input("Enter a URL: ")
    soup = get_web_response(user_url)
    tag_list = get_tags(soup)
    for num, tag in enumerate(tag_list):
        print(f"{num + 1}, {tag}")
    user_tag = int(input("\nWhat tag will you like to inspect (Enter the corresponding number): "))
    print(get_tag_elements(soup, tag_list, user_tag))


def get_tags(obj):
    tags = []
    for tag in obj.find_all():
        if tag.name in tags:
            continue
        tags.append(tag.name)
    return tags


def get_tag_elements(soup, tag_list, tag_number):
    active_tag = soup.find(tag_list[tag_number - 1])
    active_tag_attr = active_tag.attrs.keys()
    active_tag_list = get_tags(active_tag)
    active_tag_string = active_tag.string if active_tag.string else "N/A"
    return active_tag_attr, active_tag_list, active_tag_string


def get_web_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        return soup
    return response.status_code


if __name__ == "__main__":
    main()
