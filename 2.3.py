n, m = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        a.append([x[j], i, j])
b = [-1] * n
c = [-1] * m
a.sort(key = lambda f: f[0])
for i in range(n * m):
    b[a[i][1]] = a[i][2]
    if c[a[i][2]] == -1:
        c[a[i][2]] = a[i][1]
s = 0
for i in range(n):
    if i == c[b[i]]:
        print(i + 1, b[i] + 1)
        s += 1
if s == 0:
    print('none')