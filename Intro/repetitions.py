import sys

data = sys.stdin.readline()

lf = 0
freq = 0
char = ''
for i in range(len(data)):
    if data[i] == char:
        freq += 1
    else:
        lf = max(lf, freq)
        freq = 1
        char = data[i]
print(lf)