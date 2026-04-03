import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


nums.sort()
ans = 1
for i in range(1, len(nums)):
    if nums[i-1] != nums[i]:
        ans += 1
print(ans)

# print(len(set(nums)))