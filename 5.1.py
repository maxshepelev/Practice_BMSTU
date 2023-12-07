n, k, tp = map(int, input().split())
a = list(map(int, input().split()))
if tp == 1:
    if a[0] > k or a[-1] < k:
        print(-1)
    else:
        l = -1
        r = n
        while r - l > 1:
            m = (r + l) // 2
            if a[m] < k:
                l = m
            else:
                r = m
        if a[r] == k:
            print(r + 1)
        else:
            print(-1)
else:
    if a[0] < k or a[-1] > k:
        print(-1)
    else:
        l = -1
        r = n
        while r - l > 1:
            m = (r + l) // 2
            if a[m] > k:
                l = m
            else:
                r = m
        if a[r] == k:
            print(r + 1)
        else:
            print(-1)