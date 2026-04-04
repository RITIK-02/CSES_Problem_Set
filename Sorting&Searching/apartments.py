import sys

input = sys.stdin.readline

n, m, k = tuple(map(int, input().split()))
des = list(map(int, input().split()))
avail = list(map(int, input().split()))

ans = 0

des.sort()
avail.sort()
i = 0
j = 0
while i < n and j < m:
    if des[i] - k <= avail[j] <= des[i] + k:
        ans += 1
        i += 1
        j += 1
    elif des[i] + k < avail[j]:
        i += 1
    elif des[i] - k > avail[j]:
        j += 1

print(ans)
