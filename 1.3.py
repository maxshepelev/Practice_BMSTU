x = int(input())
ans = ''
s1 = 1
s2 = 2
while s2 <= x:
    s1, s2 = s2, s1 + s2
while s2 > 1:
    if x >= s1:
        ans += '1'
        x -= s1
    else:
        ans += '0'
    s1, s2 = s2 - s1, s1
print(ans)