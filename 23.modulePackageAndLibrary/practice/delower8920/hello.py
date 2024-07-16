def format_info (name,age,city):
    return f"Name: {name}, Age: {age}, City: {city}"

person_info = {
    "name": "Delower",
    "age": 22,
    "city": "Pabna"
}

helo = format_info(**person_info)
print("Person information:", helo)



def triangle_area (b,h):
    print(f"The area of the triangle is: {0.5*b*h} square unit")


def rectangle_area (a, b):
    print(f"The area of the rectangle  is: {a*b} square unit")


def add (a,b):
    print(a+b)

