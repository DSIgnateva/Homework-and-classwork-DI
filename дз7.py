import math


class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, new):
        new_x = self.x + new.x
        new_y = self.y + new.y
        return Vector2D(new_x, new_y)

    def add2(self, new):
        self.x += new.x
        self.y += new.y

    def sub(self, new):
        new_x = self.x - new.x
        new_y = self.y - new.y
        return Vector2D(new_x, new_y)

    def sub2(self, new):
        self.x -= new.x
        self.y -= new.y

    def mult(self, num):
        new_x = self.x * num
        new_y = self.y * num
        return Vector2D(new_x, new_y)

    def mult2(self, num):
        self.x *= num
        self.y *= num

    def str(self):
        return 'Vector2D(x = ' + str(self.x) + ', y = ' + str(self.y) + ')'

    def len(self):
        return len((self.x ** 2 + self.y ** 2) ** 0.5)

    def scalarProduct(self, new):
        prod = self.x * new.x + self.y + new.y
        return Vector2D(prod)

    def cos(self, new):
        cs = (self.x * new.x + self.y * new.y) / ((self.x ** 2 + self.y ** 2) ** 0.5 * (new.x ** 2 + new.y ** 2) ** 0.5)
        return Vector2D(cs)

    def equals(self, new):
        len_old = (self.x ** 2 + self.y ** 2) ** 0.5
        len_new = (new.x ** 2 + new.y ** 2) ** 0.5
        if len_old > len_new:
            return 'Первый вектор длины ' + str(len_old) + ' больше'
        elif len_old < len_new:
            return 'Второй вектор длины ' + str(len_new) + ' больше'
        else:
            return 'Оба вектора длины ' + str(len_new) + ' = ' + str(len_old) + ' одинаковы'


class RationalFraction():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reduce(self):
        if self.x > self.y:
            a = self.x
        else:
            a = self.y
        while a != 1:
            if self.x % a == 0 and self.y % a == 0:
                return self.x // a, self.y // a
            else:
                a -= 1
        return self.x, self.y

    def add(self, new):
        if self.y == new.y:
            new_x = self.x + new.x
            new_y = self.y
        else:
            new_x = self.x * new.y + new.x * self.y
            new_y = self.y * new.y
        return RationalFraction(new_x, new_y).reduce()

    def add2(self, new):
        if self.y == new.y:
            self.x = self.x + new.x
            self.y = self.y
        else:
            self.x = self.x * new.y + new.x * self.y
            self.y = self.y * new.y

    def sub(self, new):
        if self.y == new.y:
            new_x = self.x - new.x
            new_y = self.y
        else:
            new_x = self.x * new.y - new.x * self.y
            new_y = self.y * new.y
        return RationalFraction(new_x, new_y).reduce()

    def sub2(self, new):
        if self.y == new.y:
            self.x = self.x - new.x
            self.y = self.y
        else:
            self.x = self.x * new.y - new.x * self.y
            self.y = self.y * new.y

    def mult(self, new):
        new_x = self.x * new.x
        new_y = self.y * new.y
        return RationalFraction(new_x, new_y).reduce()

    def mult2(self, new):
        self.x = self.x * new.x
        self.y = self.y * new.y

    def div(self, new):
        new_x = self.x * new.y
        new_y = new.x * self.y
        return RationalFraction(new_x, new_y).reduce()

    def div2(self, new):
        self.x = self.x * new.y
        self.y = self.y * new.x

    def str(self):
        return str(self.x) + '/' + str(self.y)

    def value(self):
        return self.x / self.y

    def equals(self, new):
        if self.x / self.y > new.x / new.y:
            return 'Первая дробь ' + str(self.x) + '/' + str(self.y) + ' больше'
        elif self.x / self.y < new.x / new.y:
            return 'Вторая дробь ' + str(new.x) + '/' + str(new.y) + ' больше'
        else:
            return 'Значения дробей равны ' + str(self.x) + '/' + str(self.y) + ' = ' + str(new.x) + '/' + str(new.y)

    def numberPart(self):
        return int(self.x / self.y)


class ComplexNumber():
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def add(self, new):
        new_a = self.a + new.a
        new_b = self.b + new.b
        return ComplexNumber(new_a, new_b)

    def add2(self, new):
        self.a += new.a
        self.b += new.b

    def sub(self, new):
        new_a = self.a - new.a
        new_b = self.b - new.b
        return ComplexNumber(new_a, new_b)

    def sub2(self, new):
        self.a -= new.a
        self.b -= new.b

    def multNumber(self, num):
        new_a = self.a * num
        new_b = self.b * num
        return ComplexNumber(new_a, new_b)

    def multNumber2(self, num):
        self.a *= num
        self.a *= num

    def mult(self, new):
        new_a = self.a * new.a - self.b * new.b
        new_b = self.a * new.b + self.b * new.a
        return ComplexNumber(new_a, new_b)

    def mult2(self, new):
        self.a = self.a * new.a - self.b * new.b
        self.b = self.a * new.b + self.b * new.a

    def div(self, new):
        new_a = (self.a * new.a + self.b * new.b) / ((new.a) ** 2 - (new.b) ** 2)
        new_b = (self.b * new.a - self.a + new.b) / ((new.a) ** 2 - (new.b) ** 2)
        return ComplexNumber(new_a, new_b)

    def div2(self, new):
        self.a = (self.a * new.a + self.b * new.b) / ((new.a) ** 2 - (new.b) ** 2)
        self.b = (self.b * new.a - self.a + new.b) / ((new.a) ** 2 - (new.b) ** 2)

    def len(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def str(self):
        if self.b > 0:
            return f'{self.a} + {self.b} * i'
        else:
            return f'{self.a} - {self.b} * i'

    def arg(self):
        return math.degrees(math.atan(self.a / self.b))

    def pow(self, num):
        f = self.arg()
        coef = self.len() ** num
        self.a = coef * math.cos(f * num)
        self.b = coef * math.sin(f * num)

    def equals(self, new):
        if (self.a ** 2 + self.b ** 2) ** 0.5 > (new.a ** 2 + new.b ** 2) ** 0.5:
            return f'Первое число {self.a} + {self.b} * i больше'
        elif (self.a ** 2 + self.b ** 2) ** 0.5 < (new.a ** 2 + new.b ** 2) ** 0.5:
            return f'Второе число {new.a} + {new.b} * i больше'
        else:
            return 'Значения чисел равны'