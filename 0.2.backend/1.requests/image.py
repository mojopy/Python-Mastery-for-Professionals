import requests
r = requests.get("https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg")

with open("cat.jpg", "wb") as f:
    f.write(r.content)