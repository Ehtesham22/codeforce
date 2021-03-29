word = input()
is_small = []
is_capital = []
for x in range(0, len(word)):
    if word[x].islower():
        is_small.append(x)
    else:
        is_capital.append(x)
if len(is_small) > len(is_capital):
    print(word.lower())
elif len(is_small) == len(is_capital):
    print(word.lower())
else:
    print(word.upper())
