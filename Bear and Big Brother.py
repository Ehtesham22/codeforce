a, b = [int(x) for x in input().split()]
count = 0
while not (a > b):
    a = a * 3
    b = b * 2
    count += 1
print(count)
# 4 9
