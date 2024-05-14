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
        for tag in tag_elements:
            print(f"Attributes in tag '{tag.name}': {get_tag_attributes(tag)}")
            print(f"Child tags in tag '{tag.name}': {get_child_tags(tag)}")
            print(f"String in tag '{tag.name}': {get_tag_string(tag)}" if get_tag_string(tag)
                  else "No strings in this tag")
            print("\n-----------------------------------------------------------------------------------------------\n")


def get_child_tags(tag):
    """Get all the child tags of a particular tag."""
    tags = []
    for child_tag in tag.find_all():
        if child_tag.name in tags:
            continue
        tags.append(child_tag.name)
    return tags


def get_tag_elements(tag, tag_list, tag_number):
    """Get all tags that match the user's tag."""
    for active_tag in tag.find_all(tag_list[tag_number - 1]):
        yield active_tag


def get_tag_attributes(tag):
    """Get the attributes within a tag."""
    tag_attr = [key for key in tag.attrs.keys()]
    return tag_attr


def get_tag_string(tag):
    """Get the string within a tag."""
    tag_string = tag.string
    return tag_string


def get_web_response(url):
    """Get the webpage document and parse it."""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        return soup
    return response.status_code


if __name__ == "__main__":
    main()
