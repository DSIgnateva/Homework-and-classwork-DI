# задача 4

a, b = sorted(list("автор")), sorted(list('товар'))
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            print('не анаграмма')
            break
    else:
        print('анаграмма')

# задача 5

a = [1, 2, 3, 4]
for i in range(len(a)):
    a[i] = f'{a[i]}'
b = int(''.join(a))
a = list(str(b + 1))
print(a)

# задача 6

n = 6
s = [3, 2, 7, 1, 9, 3]
for i in range(len(s)):
    if s[i] < n:
        if (n - s[i]) in s:
            print(s[i], n - s[i])
            break
else:
    print('нет таких чисел')

# задача 7

print('даша'[::-1])

# задач 8

a, b = 'А роза, упала на, лапу Азора'.lower(), ''
for elem in a:
    if elem.isalpha():
        b += elem
if b == b[::-1]:
    print('палиндром')
else:
    print('не палиндром')






