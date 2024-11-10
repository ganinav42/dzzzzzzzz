#Задача A
p = []
k = int(input())
for i in range(k):
    s = str(input())
    p += [s[0]]  
q = 0 
print(p)
for i in range(k):
    if p[i] == "а" or p[i] == "б" or p[i] == "в":
        q += 1
    else:
        q += 0
print(k, q)
if k == q:
    print("YES")
else:
    print('NO')

#Задача B
s = list(input())    
print(" \n".join(s))

#Задача C
dl = int(input())
kol = int(input())
for i in range(kol):
    ans = input()
    if len(ans) <= dl:
        print(ans)
    else:
        print(ans[0:dl-3] + "...")

#Задача D
while (n := input()):
    if not n.endswith('@@@'):
        if n.startswith('##'):
            print(n[2:])
        else:
            print(n)

#Задача E
print('YES' if (line := input()) == line[::-1] else 'NO')

#Задача F
counter = 0
for _ in range(int(input())):
    counter += input().count("зайка")
print(counter)

#Задача G
print(sum(map(int, input().split())))

#Задача H
for _ in range(int(input())):
    if "зайка" in (place := input()):
        print(place.index("зайка") + 1)
    else:
        print("Заек нет =(")

#Задача I
while (n := input()):
    if not n.startswith('#'):
        print(n[:(n.index('#') if '#' in n else len(n))])

#Задача J
data = []
while (n := input()) != 'ФИНИШ':
    data.extend(n.lower().split())
max_count, data = 0, ''.join(data)
for symbol in set(data):
    max_count = max(max_count, data.count(symbol))
print(min([i for i in set(data) if data.count(i) == max_count]))

#Задача K
headings = []
for _ in range(int(input())):
    headings.append(input())
word = input()
for heading in headings:
    if word.lower() in heading.lower():
        print(heading)

#Задача L
order = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')
for i in range(int(input())):
    print(order[i % len(order)])

#Задача M
data = []
for _ in range(int(input())):
    data.append(int(input()))
number = int(input())
for i in data:
    print(i ** number)

#Задача N
data = list(map(int, input().split()))
number = int(input())
for i in data:
    print(i ** number, end=' ')

#Задача O
numbers = list(map(int, input().split()))
a = numbers[0]
while len(numbers) > 1:
    b = numbers[1]
    while b:
        a, b = b, a % b
    numbers.pop(1)
print(a)

#Задача P
length, line = int(input()), []
for _ in range(int(input())):
    line.append(input())
for i in line:
    if length > 3:
        print(i[:length - 3] + "..." if len(i) >= length - 3 else (i + "..." if length == 4 else i))
        length -= len(i)

