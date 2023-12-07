def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def compare(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def bubblesort(a, n):
    for i in range(n // 2):
        for j in range(1, n - i):
            if compare(a[j - 1], a[j]) == 1:
                swap(a, j - 1, j)
        for j in range(n - i - 2, i, -1):
            if compare(a[j - 1], a[j]) == 1:
                swap(a, j - 1, j)

n = int(input())
a = list(map(int, input().split()))
bubblesort(a, n)
print(*a)