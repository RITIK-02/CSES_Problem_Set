n = int(input())

arr = []

s = set(range(1,n+1))

# while s:
#     flag = True
#     for i in range(1,n+1):
#         if i in s and (not arr or abs(arr[-1] - i) > 1):
#             arr.append(i)
#             s.remove(i)
#             flag = False
#     if (flag):
#         break

for i in range(2, n+1, 2):
    if i in s:
        arr.append(i)
        s.remove(i)
if (not arr or (arr and abs(arr[-1] - 1) > 1)):
    for i in range(1, n+1, 1):
        if i in s:
            arr.append(i)
            s.remove(i)
    

if (len(arr) == n):
    for i in arr:
        print(i, end=' ')
else:
    print("NO SOLUTION")
