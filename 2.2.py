def primediv(x):
    k = abs(x)
    ans = 0
    a = [0] * (k + 1)
    for i in range(2, k + 1):
        if a[i] == 0:
            if k % i == 0:
                ans = i
            for j in range(i, k + 1, i):
                a[j] = 1
    if ans == 0:
        return 'No prime divisor found'
    else:
        return ans

x = int(input())
print(primediv(x))