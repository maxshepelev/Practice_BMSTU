def f(s):
    global a
    global n
    global p
    global ans
    if len(s) == n:
        k = 0
        for i in range(n):
            if s[i] == '1':
                k += a[i]
        if k in p:
            ans += 1
    else:
        f(s + '1')
        f(s + '0')


n = int(input())
a = list(map(int, input().split()))
p = set()
ans = 0
l = 1
if n == 1:
    if a[0] == 1:
        print(1)
    else:
        print(0)
else:
    while l <= 10 ** 7:
        p.add(l)
        l *= n
    f('')
    print(ans)