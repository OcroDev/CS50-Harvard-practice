people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def  f(person):
    return person["house"]

people.sort(key=f)

print(people) #sort by house


people.sort(key = lambda person: person["name"]) #lambda is an anonimous function

print(people) #sort by name 