import random
y = random.randrange(0,30)
c = 0
while c<5:
    c += 1
    x = int(input("Vnesi stevilo: "))
    if x == y:
        print("Bravo")
        break
    elif x > y:
        print("Prevec")
    else:
        print("Premalo.")

print("Nimas vec poskusov.")
