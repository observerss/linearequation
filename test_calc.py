#!/usr/bin/env python
from calc import next_token, calc

def test_next_token():
    assert next_token('1234+34', 0) == (1234, 4)
    assert next_token('1234+34', 5) == (34, 7)
    assert next_token('-3.50*3', 1) == (3.5, 5)


def test_calc():
    assert calc('1+2*3') == 7
    assert calc('1*2+3') == 5
    assert calc('(1+2)*3') == 9
    assert calc('1/(3-2)*4') == 4
    assert calc('3*2+4*1+(4+9)*6') == 88


