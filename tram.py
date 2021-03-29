number_of_stops = int(input())
capacity = []
for x in range(0, number_of_stops):
    exed, entering = [int(x) for x in input().split()]
    current_capacity = (entering[x] - exed[x])
    capacity.append(current_capacity)
capacity.sort()
print(capacity[-1])
