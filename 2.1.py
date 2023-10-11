def maxk(a, k, n):
    s = 0
    for i in range(k):
        s += a[i]
    m = s
    for i in range(k, n):
        s += a[i]
        s -= a[i - k]
        m = max(m, s)
    return m

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(maxk(a, k, n))