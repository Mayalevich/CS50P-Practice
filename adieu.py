import inflect

p = inflect.engine()
names = []

try:
    while True:
        name = input("Name: ")
        if name:
            names.append(name.strip())
except EOFError:
    pass

farewell = f"Adieu, adieu, to {p.join(names)}"
print(farewell)
