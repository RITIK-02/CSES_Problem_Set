import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

ans = 0
max_ele = arr[0]
for i in range(1, n):
    ans += max(0, max_ele - arr[i])
    max_ele = max(max_ele, arr[i])
print(ans)