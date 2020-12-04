import math
n, w, h = [int(x) for x in input().split()]
match = [int(input()) for m in range(n)]

max_len = math.sqrt(w**2+h**2)
for i in range(n):
    if match[i] <= max_len:
        print('DA')
    else:
        print('NE')
