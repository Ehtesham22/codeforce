# m = int(input())
# word = input()
# word = word.lower()
# a = set()
# for i in word:
#     a.add(i)

# if len(a) == 26:
#     print('YES')
# else:
#     print('NO')

n = int(input())
li = []
d = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
for i in range(n):
    li.append(input())
su = 0
for i in li:
    su += d[i]
print(su)
