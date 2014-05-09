#!/usr/bin/env python
""" Math expr solver  """
from calc import calc

EQS = [
    "3*x + 5 = 3",
    "x - 2*x + 5*x - 46*(235-24) = x + 2",
    "2*x + 5 - (3*x-2)=x + 5",
    "2*x+5-(4*x-7+(4-2))=10*x-9",
]


def solve(equation, sym='x'):
    """ solving a*x + b = 0

    for any form of a*x + b

    let x = 1, => a + b -> v1
    let x = 0, => b -> v2

    => b = v2, a = v1 - b = v1 - v2
    x = -b/a = -v2/(v1-v2)
    """
    expr = equation.replace('=', '-(') + ')'
    expr = expr.replace(' ', '')
    val1 = calc(expr.replace(sym, '1'))
    val2 = calc(expr.replace(sym, '0'))
    return 1.*(-val2)/(val1-val2)

if __name__ == '__main__':
    for eq in EQS:
        print(eq, solve(eq))
