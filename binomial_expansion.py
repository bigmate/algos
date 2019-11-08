SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


class Term(object):
    def __init__(self, val: str, power: int):
        self.val = val
        self.pow = power

    def __str__(self):
        if self.pow == 0:
            return '1'
        if self.pow == 1:
            return self.val
        return f'{self.val}{self.pow}'.translate(SUP)

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        if type(self) != type(other):
            return NotImplemented
        if self.val == other.val:
            self.pow += other.pow
            return str(self)
        if self.pow == other.pow == 0:
            return '1'
        if self.pow == other.pow == 1:
            return f'{self.val}{other.val}'
        if self.pow == other.pow:
            return f'({self.val}{other.val}){self.pow}'.translate(SUP)
        if str(self) is '1':
            return str(other)
        if str(other) is '1':
            return str(self)
        return f'{self}{other}'


class Binomial(object):
    def __init__(self, a: str, b: str, power: int):
        self.pow = power
        self.a = a
        self.b = b
        self.factorials = {}

    def coeff(self, order: int):
        return self.f(self.pow) // (self.f(order) * self.f(self.pow - order))

    def f(self, n: int):
        if n in self.factorials:
            return self.factorials[n]
        total = 1
        for i in range(1, n + 1):
            total *= i
        self.factorials[n] = total
        return total

    def _expand(self):
        for i in range(self.pow + 1):
            a = Term(self.a, self.pow - i)
            b = Term(self.b, i)
            if self.coeff(i) == 1:
                yield f'{a * b}'
            else:
                yield f'{self.coeff(i)}{a * b}'

    def expand(self):
        return '+'.join(self._expand())


if __name__ == '__main__':
    binom = Binomial('a', 'b', 6)
    print(binom.expand())
