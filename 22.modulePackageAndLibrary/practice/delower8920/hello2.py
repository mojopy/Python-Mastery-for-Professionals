print("every one want to be happy in life")


import requests
r = requests.get("https://www.istockphoto.com/photo/cute-ginger-cat-gm1443562748-482502032")

with open("cat.jpg", "wb") as f:
    f.write(r.content)





