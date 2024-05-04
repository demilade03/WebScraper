import requests

user_url = input("Enter a URL: ")
response = requests.get(user_url, headers={"Accept-Language": "en-US,en;q=0.5"})

if response.status_code == 200:
    page_content = response.content
    with open("source.html", "wb") as file:
        file.write(page_content)
    print("Contents saved")
else:
    print(f"The URL returned {response.status_code}!")
