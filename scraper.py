import requests
from bs4 import BeautifulSoup


def main():
    user_url = input("Enter a URL: ")
    soup = get_web_response(user_url)
    if isinstance(soup, int):
        print(soup)
    else:
        tag_list = get_child_tags(soup)
        for num, tag in enumerate(tag_list):
            print(f"{(num + 1):3d}. {tag}")
        user_tag = int(input("\nWhat tag will you like to inspect (Enter the corresponding number): "))
        tag_elements = get_tag_elements(soup, tag_list, user_tag)
        print(f"Attributes in tag '{tag_elements.name}': {get_tag_attributes(tag_elements)}")
        print(f"Child tags in tag '{tag_elements.name}': {get_child_tags(tag_elements)}")
        print(f"String in tag '{tag_elements.name}': {get_tag_string(tag_elements)}" if get_tag_string(tag_elements)
              else "No Strings in this tag")


def get_child_tags(obj):
    tags = []
    for tag in obj.find_all():
        if tag.name in tags:
            continue
        tags.append(tag.name)
    return tags


def get_tag_elements(tag, tag_list, tag_number):
    active_tag = tag.find(tag_list[tag_number - 1])
    return active_tag


def get_tag_attributes(tag):
    tag_attr = [key for key in tag.attrs.keys()]
    return tag_attr


def get_tag_string(tag):
    tag_string = tag.string if tag.string else ""
    return tag_string


def get_web_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        return soup
    return response.status_code


if __name__ == "__main__":
    main()
