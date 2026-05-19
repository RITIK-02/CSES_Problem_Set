import sys

input = sys.stdin.readline

n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]

start = [(i[0], 1) for i in intervals]
end = [(i[1], -1) for i in intervals]

time = start + end

time.sort(key= lambda x: x[0])

ans = 0
count = 0
for t in time:
    count += t[1]
    ans = max(count, ans)
print(ans)