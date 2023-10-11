n = int(input())
k = int(input())
ans = 0
for i in range(2, n + 1):
    ans = ((k - 1) % (i - 1) + ans) % (i - 1) + 1
print(ans)