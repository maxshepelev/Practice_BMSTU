n = int(input())
x = int(input())
p = 0
p1 = 0
for i in range(n - 1, -1, -1):
    a = int(input())
    p *= x
    p += a
    p1 *= x
    p1 += a * i
p1 //= x
print(p)
print(p1)