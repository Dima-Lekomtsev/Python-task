a = int(input())
s = a % 10
d = (a // 10) % 10
f = a // 100
print(str(s + d + f))
print(str(d + s + f))
print(str(f + s + d))
print(str(f + d + s))
print(a)
print(str(d + f + s))