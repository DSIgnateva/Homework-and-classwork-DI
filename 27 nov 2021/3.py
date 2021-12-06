n = 1234
n = [int(i) for i in list(str(n))]
s = 0
l = len(n)
for i in range(l):
    s += (-1) ** i * n[- i - 1]
print(s)