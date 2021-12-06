a = [[0, 1, 2, 3, 4], [4, 1, 3, 0, 2]]
b = [[0, 1, 2, 3, 4], [3, 2, 0, 4, 1]]
a[0], b[0] = sorted(a[0]), sorted(b[0])
for i in range(len(a[0])):
    a[1][i] = b[1][a[1][i]]
print(a)