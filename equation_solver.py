import re
from functools import reduce
from abc import ABC, abstractmethod
from typing import List, Tuple
from enum import IntEnum


class TermType(IntEnum):
    COEFFICIENT = 0
    VARIABLE = 1


class Term(ABC):
    def __init__(self, coeff: int):
        self.coeff = coeff

    def negate(self):
        self.coeff *= -1

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        return str(self)

    @abstractmethod
    def __add__(self, other):
        raise NotImplementedError

    @property
    @abstractmethod
    def type(self) -> TermType:
        raise NotImplementedError


class Variable(Term):
    def __init__(self, coeff: int, var: str):
        super().__init__(coeff)
        self.var = var

    def __str__(self):
        return f"{self.coeff}{self.var}"

    def __add__(self, other):
        return Variable(self.coeff + other.coeff, self.var)

    @property
    def type(self) -> TermType:
        return TermType.VARIABLE


class Coefficient(Term):
    def __str__(self):
        return f"{self.coeff}"

    def __add__(self, other):
        return Coefficient(self.coeff + other.coeff)

    @property
    def type(self) -> TermType:
        return TermType.COEFFICIENT


class Equation:
    EQ = re.compile(r"(\+|\-)?\s*(\d+\s*\w+|\d+|\w+)")

    def __init__(self, equation: str):
        sides = equation.split("=")
        if len(sides) != 2:
            raise ValueError(f"Invalid equation: {equation}")

        left = self.parse(sides[0])
        right = self.parse(sides[1])

        for term in right[0]:
            term.negate()
        for term in left[1]:
            term.negate()

        left[0].extend(right[0])
        right[1].extend(left[1])

        self.left = reduce(lambda x, y: x + y, left[0], Variable(0, "x"))
        self.right = reduce(lambda x, y: x + y, right[1], Coefficient(0))

    def __str__(self):
        return f"{str(self.left)}\n{str(self.right)}"

    @property
    def x(self):
        if self.left.coeff == self.right.coeff == 0:
            return "Infinite solutions"
        if self.left.coeff == 0:
            return "No solution"
        return f"x={self.right.coeff // self.left.coeff}"

    @staticmethod
    def parse(exp: str) -> Tuple[List[Variable], List[Coefficient]]:
        var = []
        coeff = []
        matches = Equation.EQ.finditer(exp)
        for _, match in enumerate(matches, start=1):
            sign, term = match.groups()
            if term.isdigit():
                t = Coefficient(int(term))
                t.coeff *= (-1 if sign is "-" else 1)
                coeff.append(t)
            else:
                num = "".join(d for d in term if d.isdigit())
                alpha = "".join(a for a in term if a.isalpha())
                t = Variable(int(num or 1), alpha)
                t.coeff *= (-1 if sign is "-" else 1)
                var.append(t)
        return var, coeff


if __name__ == '__main__':
    e = Equation("2x=x+5")
    print(e.x)
