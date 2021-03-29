n = int(input())
count = 0
for x in range(0, n):
    friend_1, friend_2, friend_3 = [int(x) for x in input().split()]
    vote = friend_1 + friend_2 + friend_3
    if vote >= 2:
        count += 1

print(count)
