k = int(input())
a, b = 1, 0

for _ in range(k):
    temp = a + b
    a = b
    b = temp
print(a, b)