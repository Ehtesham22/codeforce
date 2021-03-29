n = int(input())
winner = input()
a = winner.count('A')
d = winner.count('D')
if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')