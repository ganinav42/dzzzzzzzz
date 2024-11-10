#Задача A
s = int(input())
for i in range(1, s + 1):
    j = ''
    for k in range(1, s + 1):
        j = j + str(i * k) + ' '
    print(j)

#Задача B
s = int(input())
for i in range(1, s + 1):
    j = ''
    for k in range(1, s + 1):
        print(f"{k} * {i} = {i * k}")

#Задача C
n = int(input())
s = 1
for i in range(1, n + 1):
    for j in range(i):
        if s <= n:
            print(s, end=' ')
            s += 1
    print()

#Задача D
t = 0
k = int(input())
for s in range(k):
    a = int(input())
    for i in range(len(str(a))):
        t += int(str(a)[i])
print(t)

#Задача E
s = int(input())
y = 0
for i in range(s):
    flag = 0
    while True:
        k = input()
        if k == "ВСЁ":
            break
        else:
            if k == "зайка":
                flag = 1
    if flag == 1:
        y += 1
print(y)

#Задача F
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
gcd = numbers[0] 
for i in range(1, N):
    a = gcd
    b = numbers[i]
    while b != 0:
        a, b = b, a % b
    gcd = a 
print(gcd)

#Задача G
N = int(input())
for participant in range(1, N + 1):
    delay = participant + 2
    for seconds in range(delay, 0, -1):
        print(f"До старта {seconds} секунд(ы)")
    print(f"Старт {participant}!!!")

#Задача H
N = int(input())
winner_name = ""
max_digit_sum = -1
for _ in range(N):
    name = input().strip()  
    number = input().strip()  
    digit_sum = sum(int(digit) for digit in number)
    if digit_sum >= max_digit_sum: 
        max_digit_sum = digit_sum
        winner_name = name  
print(winner_name)

#Задача I
N = int(input())
max_digits = []
for _ in range(N):
    number = input()
    max_digit = max(number)
    max_digits.append(max_digit)
big_number = ''.join(max_digits)
print(big_number)

#Задача J
n = int(input())
print("А Б В")
for a in range(1, n - 1):  
    for b in range(1, n - a):  
        c = n - a - b  
        if c >= 1:
            print(a, b, c)

#Задача K
N = int(input())
numbers = [int(input()) for _ in range(N)]
prime_count = 0
for number in numbers:
    if number < 2:
        continue  
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1
print(prime_count)

#Задача L
N = int(input())
M = int(input())
current_number = 1
width = len(str(N * M))
for i in range(N):
    row = []
    for j in range(M):
        row.append(str(current_number).rjust(width))
        current_number += 1
    print(" ".join(row))

#Задача M
N = int(input())
M = int(input())
rectangle = []
for i in range(N):
    row = []
    for j in range(M):
        value = (i + 1) + j * N
        row.append(value)
    rectangle.append(row)
max_width = len(str(rectangle[-1][-1])) 
for row in rectangle:
    print(" ".join(f"{num:>{max_width}}" for num in row))

#Задача N
N = int(input())
M = int(input())
snake = []
counter = 1
for i in range(N):
    row = []
    for j in range(M):
        row.append(counter)
        counter += 1
    if i % 2 == 1:  
        row.reverse()
    snake.append(row)
max_width = len(str(snake[-1][-1])) 
for row in snake:
    print(" ".join(f"{num:>{max_width}}" for num in row))

#Задача O
N = int(input())
M = int(input())
snake = [[0] * M for _ in range(N)]
num = 1
for col in range(M):
    if col % 2 == 0:
        for row in range(N):
            snake[row][col] = num
            num += 1
    else:
        for row in range(N - 1, -1, -1):
            snake[row][col] = num
            num += 1
max_width = len(str(N * M))
for row in snake:
    print(" ".join(f"{x:>{max_width}}" for x in row))

#Задача P
size = int(input())
width = int(input())
cell_format = f"{{:^{width}}}"
for i in range(1, size + 1):
    row = " | ".join(cell_format.format(i * j) for j in range(1, size + 1))
    print(row.replace(' | ', '|'))
    if i < size:
        print('-' * (size * (width + 1) - 1))

