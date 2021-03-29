num = int(input())
word_list = []
for x in range(0, num):
    word = input()
    word_list.append(word)

for x in word_list:
    if len(x) > 100:
        print("the size is greater than 100")
    elif len(x) <= 10:
        print(x)
    elif len(x) > 10:

        middle_length = str(len(x) - 2)

        print(x[0] + middle_length + x[-1])
