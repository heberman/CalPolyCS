"""Functions for postfix evaluation.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

from this import d
from stack_array import *


def postfix_eval(in_str):
    """Evaluates expression in postfix notation.
    Args:
        in_str (str): input expression in RPN
    Returns:
        int: returns result from expression
    """
    stack = StackArray()
    exp = in_str.split()
    for item in exp:
        try:
            stack.push(int(item))
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if item == '+':
                stack.push(val2 + val1)
            elif item == '-':
                stack.push(val2 - val1)
            elif item == '*':
                stack.push(val2 * val1)
            elif item == '/':
                if val1 == 0:
                    raise ValueError()
                stack.push(val2 / val1)
            elif item == '^':
                stack.push(val2 ** val1)
    return stack.pop()


def infix_to_postfix(in_str):
    """Converts an infix expression to postfix
    Args:
        in_str (str): input expression in infix notation
    Returns:
        str: returns expression in RPN
    """
    stack = StackArray()
    rpn = ''
    exp = in_str.split()
    for item in exp:
        print(rpn)
        try:
            rpn += str(item) + ' '
        except ValueError:
            if item == '(':
                stack.push(item)
            elif item == ')':
                while stack.peek() != '(':
                    rpn += stack.pop() + ' '
                stack.pop()
            else:
                if stack.is_empty():
                    stack.push(item)
                else:
                    if item == '^' or is_higher_precedence(item, stack.peek()):
                        stack.push(item)
                    else:
                        rpn += stack.pop() + ' '
                        while not stack.is_empty() and not is_higher_precedence(item, stack.peek()):
                            rpn += stack.pop() + ' '
                        stack.push(item)
    while not stack.is_empty():
        rpn += stack.pop() + ' '
    if rpn[len(rpn) - 1] == ' ':
        rpn = rpn[:len(rpn) - 1]
    return rpn


def prefix_to_postfix(in_str):
    """Converts an prefix expression to postfix
        Args:
            in_str (str): input expression in prefix notation
        Returns:
            str: returns expression in RPN
        """
    stack = StackArray()
    exp = in_str.split()
    for i in range(len(exp) - 1, -1, -1):
        try:
            stack.push(int(exp[i]))
        except ValueError:
            o1 = stack.pop()
            o2 = stack.pop()
            stack.push(str(o1) + ' ' + str(o2) + ' ' + exp[i])
    return stack.pop()


def is_higher_precedence(o1, o2):
    """Helper function for infix_to_postfix(). Evaluates precedence of two operators.
    Args:
        o1 (str): operator 1
        o2 (str): operator 2
    Returns:
        returns True if o1 has higher precedence than o2 and False if o1 has equal or lower precedence.
    """
    if o2 == '(':
        return True
    if o1 == '-' or o1 == '+':
        return False
    if o1 == '*' or o1 == '/':
        return o2 == '+' or o2 == '-'
    return True

def boof(o1, o2):
    if o2 == '(':
        return True
    if o1 == '-' or o1 == '+':
        return False
    if o1 == '*' or o1 == '/':
        if o2 == '+' or o2 == '-':
            return True
        return False
    if o1 == '^':
        if o2 == '<<' or o2 == '>>':
            return False
        return False
    if o1 == '<<' or o1 == '>>':
        return o2 != '<<' or o2 == '>>'
    return True


infix_to_postfix('6 - 3
')

