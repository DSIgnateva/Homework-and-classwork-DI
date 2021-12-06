n = 5
# s = [int(input()) for _ in range(n)] правильный вариант ввода
s = [153, 42686, 74, 8, 367]  # для более удобных тестов
count = 0
for i in range(n):
    s[i] = str(s[i])
    k = s[i]
    if len(k) == 3 or len(k) == 5:
        r = [j for j in list(k) if int(j) % 2 == 0]
        p = [j for j in list(k) if int(j) % 2 != 0]
        if len(r) == len(k) or len(p) == len(k):
            count += 1
    if count > 2:
        print('Больше двух')
        break
else:
    if count == 2:
        print('Есть')
    else:
        print('Нет таких чисел')
