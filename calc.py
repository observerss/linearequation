#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A math expr calculator using stack

"""


def next_token(string, start):
    """ given string and start index

    return token and next start index
    """
    token = string[start]
    # numbers
    if token.isdigit():
        token = int(token)
        start += 1
        float_pos = 0
        while start < len(string) and string[start] in '0123456789.':
            if string[start].isdigit():
                if float_pos:
                    token += 1. * int(string[start]) * (0.1 ** float_pos)
                    float_pos += 1
                else:
                    token = token * 10 + int(string[start])
            elif string[start] == '.':
                float_pos = 1
            start += 1
        return token, start
    # +-*/()
    else:
        return token, start + 1


def do_op(num1, num2, oper):
    """ do operations """
    if oper == '*':
        return num1 * num2
    elif oper == '/':
        return 1. * num1 / num2
    elif oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2


def calc(expr):
    """ evaluate some numeral expression """
    # operators and their priorities
    ops = {
        '(': 3,
        ')': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
    }

    # op_stack is used to push ops + '(', ')'
    # num_stack is used to push numbers
    op_stack = []
    num_stack = []

    def evaluate_last():
        """ evaluate top two numbers with top operation """
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        oper = op_stack.pop()
        num_stack.append(do_op(num1, num2, oper))

    def should_evaluate_last(tok):
        """ whether evaluate_last should be called """
        # if tok's priority is eq/lower than last tok's priority
        # last two numbers and last tok should be evaluated right now
        if len(op_stack) > 0 and\
                op_stack[-1] != '(' and\
                ops[tok] <= ops[op_stack[-1]]:
            return True
        else:
            return False

    i = 0
    while i < len(expr):
        tok, i = next_token(expr, i)
        if tok in ops:
            if len(op_stack) == 0:
                op_stack.append(tok)
            elif tok == '(':
                op_stack.append(tok)
            elif tok == ')':
                while op_stack[-1] != '(':
                    evaluate_last()
                op_stack.pop()
            else:
                while should_evaluate_last(tok):
                    evaluate_last()
                op_stack.append(tok)
        else:
            num_stack.append(tok)

    while len(num_stack) > 1:
        evaluate_last()

    return num_stack[0]
