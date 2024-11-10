# задача А
print("Привет, Яндекс!")


# задача B
print("Привет,", input("Как Вас зовут?"))


# задача C
n = input()
print(n)
print(n)
print(n)
    

# задача D
print(int(input()) - 95)


# задача E
price = int(input())
weight = int(input())
money = int(input())
total_cost = price * weight
change = money - total_cost
print(change)


# задача F
name = str(input())
price = int(input())
weight = int(input())
money = int(input())
total_cost = price * weight
change = money - total_cost
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {total_cost}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")


# задача G
for i in range(int(input())):
    print('Купи слона!')


# задача H
i = int(input())
s = str(input())
for i in range(i):
    print(f'Я больше никогда не буду писать "{s}"!')



# задача I
print(int(input()) // 2 * int(input()))


# задача J
name = str(input())
s = str(input())
print(f"Группа №{s[0]}.")
print(f"{s[2]}. {name}.")
print(f"Шкафчик: {s}.")
print(f"Кроватка: {s[1]}.")
    

# задача K
n = str(int(input()))
print(int(f"{n[1]}{n[0]}{n[3]}{n[2]}"))
    


# задача L
q = int(input())
w = int(input())
e = ((q % 10) + (w % 10)) % 10
r = ((q // 10 % 10) + (w // 10 % 10)) % 10
t = ((q // 100) + (w // 100)) % 10
print(f'{t}{r}{e}')


# задача M
children = int(input())
candies = int(input())
candies_per_child = candies // children
remaining_candies = candies % children
print(candies_per_child)
print(remaining_candies)


# задача N
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)

    
# задача O
hours = int(input())
minutes = int(input())
delivery_time = int(input())
delivery_minutes = hours * 60 + minutes + delivery_time
delivery_hours = (delivery_minutes // 60) % 24
delivery_minutes = delivery_minutes % 60
print(f"{delivery_hours:02d}:{delivery_minutes:02d}")
    

# задача P
a = int(input())
b = int(input())
c = int(input())
s = float((b - a) / c)
print(f"{s:0<4}")



# задача Q
a = int(input())
b = input()
print(a + int(b, 2))


#задача R
a = int(input())
b = int(input())
c = int(input())
x = max(a, b, c)
z = min(a, b, c)
y = a + b + c - x - z
if x ** 2 == y ** 2 + z ** 2:
    print('100%')
elif x ** 2 < y ** 2 + z ** 2:
    print('крайне мала')   
elif x ** 2 > y ** 2 + z ** 2:
    print('велика')


# задача S
tov = input()
cen = int(input())
ves = int(input())
kolvo = int(input())
s = cen * ves
sd = kolvo - s
s2 = ' ' * (35 - 6 - len(tov))
s3 = ' ' * (35 - 5 - 6 - 2 - 3 - len(str(ves)) - len(str(cen)))
s4 = ' ' * (35 - 6 - 3 - len(str(s)))
s5 = ' ' * (35 - 8 - 3 - len(str(kolvo)))
s6 = ' ' * (35 - 6 - 3 - len(str(sd)))
print('================Чек================')
print(f'Товар:{s2}{tov}')
print(f'Цена:{s3}{ves}кг * {cen}руб/кг')
print(f'Итого:{s4}{s}руб')
print(f'Внесено:{s5}{kolvo}руб')
print(f'Сдача:{s6}{sd}руб')
print('===================================')



# задача T
n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
x = ((m * n) - (n * k2)) / (k1 - k2)
y = n - x
print(int(x), int(y))
                    
    