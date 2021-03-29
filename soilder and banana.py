k, n, w = [int(x) for x in input().split()]
amount = []
for x in range(1, w+1):
    price = x*k
    amount.append(price)
total = 0
for x in range(0, len(amount)):
    total = total + amount[x]
if n < total:
    print(total - n)
else:
    print(0)
