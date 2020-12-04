a, b, c = [int(x) for x in input().split()]
dist_ab = b-a-1
dist_bc = c-b-1
max_dist = max(dist_ab, dist_bc)
print(max_dist)