# классная работа

import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(time.perf_counter() - start_time)
        return res

    return wrapped


@time_of_function
def func(first, second):
    return int(first) + int(second)


print(func("111", "10"))


# домашняя работа, задание 1


def time_of_function(function):
    def wrapped(*args):
        f1 = open("text1.txt", 'w')
        start_time = time.perf_counter()
        res = function(*args)
        f1.write(f'Функция вызвана во столько: {time.strftime("%H:%M:%S", time.localtime())}\n')
        f1.write(f'Функция выполнялась {time.perf_counter() - start_time} секунд\n')
        f1.write(f'Функция завершена во столько: {time.strftime("%H:%M:%S", time.localtime())}\n')
        return res

    return wrapped


@time_of_function
def func(first, second):
    return int(first) + int(second)


print(func("111", "10"))


# задание 2


def isprime(n):
    if n == 1:
        return False
    for x in range(2, int(n ** (1 / 2)) + 1):
        if n % x == 0:
            return False
        else:
            return True


def primes(n):
    for i in range(1, n):
        if isprime(i):
            yield i


for el in primes(10):
    print(el)
