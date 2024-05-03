import requests
from bs4 import BeautifulSoup

user_url = input("Enter a URL: ")
response = requests.get(user_url, headers={"Accept-Language": "en-US,en;q=0.5"})

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    title_tag = soup.title
    meta_tag = soup.meta
    print(title_tag.text, meta_tag)
else:
    print("Invalid quote resource!")
