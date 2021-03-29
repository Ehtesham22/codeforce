letter = input()
li = []
for char in letter:
    if char.isalpha():
        li.append(char)
a = set(li)
print(len(a))