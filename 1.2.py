a = int(input())
b = int(input())
m = int(input())
s = ''
a %= m
p = 0
while b > 0:
    s = str(b % 2) + s
    b //= 2
for i in range(len(s)):
    p *= 2
    p %= m
    p += a * int(s[i])
    p %= m
print(p)