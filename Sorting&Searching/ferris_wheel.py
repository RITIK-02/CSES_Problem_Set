import sys

input = sys.stdin.readline

n, x = tuple(map(int,input().split()))

weights = list(map(int, input().split()))

weights.sort()

ans = 0

# Naive
# vis = [0]*n
# for i in range(n):
#     if vis[i]:
#         continue
#     first = i
#     second = i
#     for j in range(i+1, n):
#         if vis[j]:
#             continue
#         if (weights[first] + weights[j] > x):
#             break
#         else:
#             second = j
#     if first == second:
#         vis[first] += 1
#     else:
#         vis[first] += 1
#         vis[second] += 1

#     ans += 1
 
i = 0
j = n-1
ans = 0
while (i <= j):
    if (weights[i] + weights[j] <= x):
       ans += 1
       i += 1
    else:
        ans += 1 
    j -= 1

print(ans)