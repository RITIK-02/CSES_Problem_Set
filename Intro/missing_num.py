# import sys
# data = sys.stdin.read().split()

# it = iter(data)

# n = int(next(it))
# nums = [int(next(it)) for _ in range(n-1)]

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

#SUM
# total = sum(nums)
# print((n*(n+1)//2) - total)

#XOR
xor_num = 0
for i in range(1, n+1):
    xor_num ^= i
    if (i < n):
        xor_num ^= nums[i-1]
print(xor_num)