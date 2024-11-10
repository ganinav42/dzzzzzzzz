#задача А
print('Как Вас зовут?')
s = input()
print(f'Здравствуйте, {s}!')
print('Как дела?')
n = input()
if n == 'хорошо':
    print('Я за вас рада!')
elif n == 'плохо':
    print('Всё наладится!')


#задача B
n = int(input())
s = int(input())
if n > s:
    print('Петя')
if n < s:
    print('Вася')


#задача C
n = int(input())
s = int(input())
k = int(input())
if n > s and n > k:
    print('Петя')
elif s > n and s > k:
    print('Вася')
elif k > n and k > s:
    print('Толя')


#задача D
n = int(input())
s = int(input())
k = int(input())
m2 = n + s + k - max(n, s, k) - min(n, s, k)
if max(n, s, k) == n:
    p = 'Петя'
elif max(n, s, k) == s:
    p = 'Вася'
elif max(n, s, k) == k:
    p = 'Толя'
v = ''
if m2 == n:
    v = 'Петя'
elif m2 == s:
    v = 'Вася'
elif m2 == k:
    v = 'Толя'
t = ''
if min(n, s, k) == n:
    t = 'Петя'
elif min(n, s, k) == s:
    t = 'Вася'
elif min(n, s, k) == k:
    t = 'Толя'
print(f'1. {p}')
print(f'2. {v}')
print(f'3. {t}')


#задача E
n = int(input())
m = int(input())
p = 6 + n
v = 12 + m
if p > v:
    print('Петя')
elif p < v:
    print('Вася')


#задача F
n = int(input())
if n % 4 == 0 and (n % 400 == 0 or n % 100 != 0):
    print('YES')
else:
    print('NO')


#задача G
n = str(int(input()))
q = n[0:2]
e = n[2:4]
e = e[::-1]
if q == e:
    print('YES')
else:
    print('NO')


#задача H
s = input()
if 'зайка' in s:
    print('YES')
else:
    print('NO')


#задача I
q = input()
w = input()
e = input()
a = q[0]
s = w[0]
d = e[0]
if min(a, s, d) == a:
    print(q)
elif min(a, s, d) == s:
    print(w)
elif min(a, s, d) == d:
    print(e)


#задача J
s = str(int(input()))
s1 = int(s[0])
s2 = int(s[1])
s3 = int(s[2])
q = s2 + s3
w = s1 + s2
e = str(max(q, w)) + str(min(q, w))
print(e)


#задача K
s = str(int(input()))
s1 = int(s[0])
s2 = int(s[1])
s3 = int(s[2])
ma = max(s1, s2, s3)
mi = min(s1, s2, s3)
m2 = s1 + s2 + s3 - ma - mi
if ma + mi == m2 * 2:
    print('YES')
else:
    print('NO')


#задача L
q = int(input())
w = int(input())
e = int(input())
if q < w + e and w < q + e and e < w + q:
    print('YES')
else:
    print('NO')


#задача M
q = str(int(input()))
w = str(int(input()))
e = str(int(input()))
if q[0] == w[0] == e[0]:
    print(q[0])
elif q[1] == w[1] == e[1]:
    print(q[1])


#задача N
p = int(input())
q = str(p)
w = int(q[0] + q[1])
e = int(q[0] + q[2])
r = int(q[1] + q[2])
t = int(q[1] + q[0])
y = int(q[2] + q[1])
u = int(q[2] + q[0])
a = min(w, e, r, t, y, u)
s = max(w, e, r, t, y, u)
if a < 10 and a != 0:
    print(int(f'{str(a)}0'), s)
elif a == 0:
    print(s, s)
else:
    print(a, s)


#задача O
p = str(int(input()))
k = str(int(input()))
q = int(p[0])
w = int(p[1])
e = int(k[0])
r = int(k[1])
a = max(q, w, e, r)
s = min(q, w, e, r)
d = (q + w + e + r - a - s) % 10
print(int(f'{a}{d}{s}'))


#задача P
q = int(input())
w = int(input())
e = int(input())
a = max(q, w, e)
d = min(q, w, e)
s = q + w + e - a - d
z = 'Петя'
x = 'Вася'
c = 'Толя'
if a == q and s == w and d == e:
    print(f"{z: ^24}")
    print(f"  {x: <22}")
    print(f"{c: >22}  ")
    print('   II      I      III ')
elif a == w and s == e and d == q:
    print(f"{x: ^24}")
    print(f"  {c: <22}")
    print(f"{z: >22}  ")
    print('   II      I      III ')
elif a == e and s == w and d == q:
    print(f"{c: ^24}")
    print(f"  {x: <22}")
    print(f"{z: >22}  ")
    print('   II      I      III ')
elif a == e and s == q and d == w:
    print(f"{c: ^24}")
    print(f"  {z: <22}")
    print(f"{x: >22}  ")
    print('   II      I      III ')
elif a == w and s == q and d == e:
    print(f"{x: ^24}")
    print(f"  {z: <22}")
    print(f"{c: >22}  ")
    print('   II      I      III ')
elif a == q and s == e and d == w:
    print(f"{z: ^24}")
    print(f"  {c: <22}")
    print(f"{x: >22}  ")
    print('   II      I      III ')


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

