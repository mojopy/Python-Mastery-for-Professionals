import requests
r = requests.get("https://en.wikipedia.org/wiki/File:Cat_August_2010-4.jpg")

with open("cat.jpg", "wb") as f:
    f.write(r.content)