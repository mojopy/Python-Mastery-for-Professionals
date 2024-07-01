from hello import *
print("delower infomration is ", helo)
rectangle_area(12,2)
triangle_area(12,2)
add(20,30)


from hello2 import requests


import requests
r = requests.get("https://www.istockphoto.com/photo/cute-ginger-cat-gm1443562748-482502032")

print(r.text)

print(r.json())

print(r.status_code)