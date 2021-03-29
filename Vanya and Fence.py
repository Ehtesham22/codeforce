n, h = [int(x) for x in input().split()]
hi = [int(x) for x in input().split()]
count = 0
for x in range(len(hi)):
    if hi[x] > h:
        count += 2
    else:
        count += 1
print(count)
