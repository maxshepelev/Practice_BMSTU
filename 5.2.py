def f(s):
    global ans
    global n
    global a
    global b
    global p
    if len(s) == n:
        k = len(a[int(s[0])])
        for i in range(1, len(s)):
            k += len(a[int(s[i])]) - b[int(s[i - 1])][int(s[i])]
        ans = min(ans, k)
    else:
        for i in p:
            if len(s) == 0 or i not in s:
                f(s + i)
            




n = int(input())
a = []
ans = 0
p = ''
for i in range(n):
    s = input()
    ans += len(s)
    a.append(s)
    p += str(i)
b = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if j != i:
            m = 0
            i2 = len(a[j]) - 1
            s1 = ''
            s2 = ''
            for i1 in range(min(len(a[j]), len(a[i]))):
                s1 += a[i][i1]
                s2 = a[j][i2] + s2
                if s1 == s2:
                    m = i1 + 1
                i2 -= 1
            b[j][i] = m
            
f('')
print(ans)