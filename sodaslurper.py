e,f,c = [int(x) for x in input().split()]

bottles = e + f
total = 0
while bottles >= c:
    bottles -= c
    total += 1
    bottles += 1
print(total)