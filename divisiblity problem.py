n = int(input())
result = []
for x in range(n):
    count = 0
    a, b = [int(x) for x in input().split()]
    while not a % b == 0:
        if a % b == 0:
            result.append(count)
        else:
            a = a+1
            count += 1
    result.append(count)
print('\n'.join(map(str, result)))

'''second method(executes in less time)'''

n = int(input())
for x in range(n):
    a, b = [int(x) for x in input().split()]
    print(-a % b)
