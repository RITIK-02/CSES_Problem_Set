# TLE due to pop function
# import sys
 
# input = sys.stdin.readline
 
# n, m = tuple(map(int, input().split()))
# h = list(map(int, input().split()))
# t = list(map(int, input().split()))
 
 
# def bs(curr, low, high):
#     if low >= high:
#         return low
#     mid = (low + high)//2+1
#     if (h[mid] <= curr):
#         return bs(curr, mid, high)
#     else:
#         return bs(curr, low, mid-1)
 
# h.sort()
# # t.sort()
# ans = []
# for i in range(m):
#     idx = bs(t[i], 0, len(h)-1)
#     if (h and t[i] >= h[idx]):
#         ans.append(h[idx])
#         h.pop(idx)
#     else:
#         ans.append(-1)
    
# for i in ans:
#     print(i)


import sys
import bisect

sys.setrecursionlimit(100000)

input = sys.stdin.readline
 
n, m = tuple(map(int, input().split()))
h = list(map(int, input().split()))
t = list(map(int, input().split()))


def find(x):
    if x == -1:
        return x
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


parent = list(range(n))

h.sort()
for i in t:
    idx = bisect.bisect_right(h, i) - 1
    avail = find(idx)
    if avail < 0:
        print(-1)
    else:
        print(h[avail])
        parent[avail] = avail-1
    
