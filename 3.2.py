#Задача A
print(''.join(set(input())))

#Задача B
print(''.join(set(input()).intersection(set(input()))))

#Задача C
objects = []
for _ in range(int(input())):
    objects.extend(input().split())
print('\n'.join(set(objects)))

#Задача D
a, b = int(input()), int(input())
semolina, oatmeal = set(), set()
for _ in range(a):
    semolina.add(input())
for _ in range(b):
    oatmeal.add(input())
both = len(semolina & oatmeal)
print(both if both else 'Таких нет')

#Задача E
a, b = int(input()), int(input())
porridges = []
for _ in range(a + b):
    porridges.append(input())
both = len([i for i in porridges if porridges.count(i) == 1])
print(both if both else 'Таких нет')

#Задача F
a, b = int(input()), int(input())
porridges = []
for _ in range(a + b):
    if (x := input()) not in porridges:
        porridges.append(x)
    else:
        porridges.remove(x)
if len(porridges):
    for kid in sorted(porridges):
        print(kid)
else:
    print('Таких нет')

#Задача G
MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' ',
}
line = input()
for letter in line:
    print(MORSE[letter.upper()], end=' ' if letter != ' ' else '\n')

#Задача H
a, kids = int(input()), []
for _ in range(a):
    kids.extend([input().split()])
kids.sort()
key, counter = input(), 0
for kid in kids:
    if key in kid[1:]:
        print(kid[0])
        counter += 1
if not counter:
    print('Таких нет')

#Задача I
d = {}
while x := input().split():
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
for j in d:
    print(j, d[j])

#Задача J
LITER = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}
for i in (x := input()):
    if i.upper() in LITER:
        print(LITER[i.upper()].lower().capitalize() if i == i.upper() else LITER[i.upper()].lower(), end='')
    else:
        print(i, end='')

#Задача K
people = []
for _ in range(int(input())):
    people.append(input())
print(len([i for i in people if people.count(i) > 1]))

#Задача L
people = []
for _ in range(int(input())):
    people.append(input())
people = [i + ' - ' + str(people.count(i)) for i in set(people) if people.count(i) > 1]
if people:
    for x in sorted(people):
        print(x)
else:
    print('Однофамильцев нет')

#Задача M
menu, new_menu = set(), set()
for _ in range(int(input())):
    menu.add(input())
for _ in range(int(input())):
    for j in range(int(input())):
        new_menu.add(input())
diff = sorted(menu - new_menu)
if diff:
    for dish in diff:
        print(dish)
else:
    print('Готовить нечего')

#Задача N
ingredients, dishes = [], set()
for _ in range(int(input())):
    ingredients.append(input())
for _ in range(int(input())):
    dishes.add(x := input())
    for i in range(int(input())):
        if input() not in ingredients:
            dishes.discard(x)
if dishes:
    for dish in sorted(dishes):
        print(dish)
else:
    print('Готовить нечего')

#Задача O
data = []
for i in list(map(lambda x: bin(int(x))[2:], input().split())):
    data.append({"digits": len(i),
                 "units": i.count('1'),
                 "zeros": i.count('0')})
print(data)

#Задача P
near = set()
while x := input().split():
    for ind, i in enumerate(x):
        if i == 'зайка' and ind not in (0, len(x) - 1):
            near.add(x[ind - 1])
            near.add(x[ind + 1])
        elif i == 'зайка' and not ind:
            near.add(x[ind + 1])
        elif i == 'зайка' and ind == len(x) - 1:
            near.add(x[ind - 1])
for item in near:
    print(item)

