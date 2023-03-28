import random
from getpass import getpass

choice = ["Kamień", "Papier", "Nożyce"]
results = []
rounds = int(input("Podaj ilość rund:\n"))
mode = int(input("Podaj tryb gry: (1- gracz vs komputer, 2- dwóch graczy (hot seats))\n"))
names = []
w1 = 0
w2 = 0
for i in range(0, mode):
    names.append(input("Podaj imie gracza " + str(i + 1) + ":\n"))
if mode == 1:
    names.append("Komputer")
for i in range(0, rounds):
    picked = int(getpass(prompt=("Gracz " + names[0] + " wybiera: (1- kamień, 2- papier, 3- nożyce\n")))
    if mode == 2:
        picked2 = int(getpass(prompt=("Gracz " + names[1] + " wybiera: (1- kamień, 2- papier, 3- nożyce\n")))
    else:
        picked2 = random.randrange(1, 4)
        print("Komputer wybiera ")
    if picked == picked2:
        tmp = "Remis!"
    else:
        if picked == 1:
            if picked2 == 3:
                tmp = ("Wygrał " + names[0])
                w1 += 1
            else:
                tmp = ("Wygrał " + names[1])
                w2 += 1
        else:
            if picked == 2:
                if picked2 == 1:
                    tmp = ("Wygrał " + names[0])
                    w1 += 1
                else:
                    tmp = ("Wygrał " + names[1])
                    w2 += 1
            else:
                if picked2 == 2:
                    tmp = ("Wygrał " + names[0])
                    w1 += 1
                else:
                    tmp = ("Wygrał " + names[1])
                    w2 += 1

    results.append(choice[picked - 1] + " vs " + choice[picked2 - 1] + " " + tmp)
    print(tmp)
    print(str(w1) + " vs " + str(w2))
print("Wyniki poszczególnych rund:")
for s in results:
    print(s)
print("Wynik ogólny:")

print(names[0] + ": " + str(w1))
print(names[1] + ": " + str(w2))
if w1 > w2:
    print("Wygrał " + names[0])
else:
    if w2 > w1:
        print("Wygrał " + names[1])
    else:
        print("Remis!")
