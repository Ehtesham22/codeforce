n = int(input())
stone = input()
count = 0
for x in range(0, len(stone)-1):
    if stone[x] == stone[x+1]:
        count += 1

print(count)