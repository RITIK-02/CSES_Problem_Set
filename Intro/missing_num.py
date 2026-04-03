import sys
data = sys.stdin.read().split()

it = iter(data)

n = int(next(it))
nums = [int(next(it)) for _ in range(n-1)]

# import sys
# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int, input().split()))

total = sum(nums)
print((n*(n+1)//2) - total)