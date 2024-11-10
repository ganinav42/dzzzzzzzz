# Задача A
while input() != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

# задача B
s = 0
while True:
    k = input()
    if k == "Приехали!":
        break
    if "зайка" in k:
        s += 1
print(s)

# задача С
s = ''
for i in range(int(input()), int(input()) + 1):
    s += str(i) + ' '
print(s)

# задача D
start = int(input())
end = int(input())
if start <= end:
    numbers = [i for i in range(start, end + 1)]
else:
    numbers = [i for i in range(start, end - 1, -1)]
print(" ".join(map(str, numbers)))

# задача E
s = 0
while True:
    k = float(input())
    if k >= 500:
        s += 0.9 * k
    if k < 500:
        s += k
    if k == 0:
        break
print(s)

# задача F
a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a)

# задача G
q = int(input())
w = int(input())
noc = 0
for i in range(q * w + 1):
    if i % q == 0 and i % w == 0:
        noc = i
    if noc != 0:
        print(noc)
        break

# задача H
q = input()
w = int(input())
for i in range(w):
    print(q)

# задача I
s = int(input())
k = 1
if s == 0:
    print(1)
else:
    for i in range(1, s + 1):
        k = k * i
print(k)

# задача J
x = 0
y = 0
while True:
    s = input()
    if s == "СТОП":
        break
    e = int(input())
    if s == "СЕВЕР":
        y = y + e
    if s == "ЮГ":
        y = y - e
    if s == "ВОСТОК":
        x = x + e
    if s == "ЗАПАД":
        x = x - e   
print(y)
print(x)

# задача K
s = input()
k = [int(s[i]) for i in range(len(s))]
print(sum(k)) 
#компилятор принял списки

# задача L
s = input()
k = [int(s[i]) for i in range(len(s))]
print(max(k)) 
#компилятор принимает списки

# задача M
s = int(input())
k = 'я'
for i in range(s):
    w = input()
    if w < k:
        k = w
print(k)

# задача N
num = int(input())
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")

# задача O
s = int(input())
k = 0
for i in range(s):
    if 'зайка' in input():
        k += 1
print(k)

# задача P
s = int(input())
if str(s) == str(s)[::-1]:
    print("YES")
else:
    print('NO')

