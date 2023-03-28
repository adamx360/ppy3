import random

# Zadanie 1
a = input("Podaj liczby:\n")
a = a.split(",")
xmin = a[0]
xmax = a[0]
for i in a[1::]:
    if i < xmin:
        xmin = i
    if i > xmax:
        xmax = i
print("max: " + xmax)
print("min: " + xmin)
# Zadanie 2

miasta = ["Warsaw", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
random.shuffle(miasta)
print(miasta)
