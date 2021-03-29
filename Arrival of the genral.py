n = int(input())
line_up = [int(x) for x in input().split()]
a = line_up.index(max(line_up))
line_up.reverse()
b = line_up.index(min(line_up))
a = int(a)
b=int(b)
if a + b >= n:
    print(a + b - 1)
else:
    print(a + b)