# Test suite to work on issue https://github.com/PyCQA/pep8/issues/399
import math
import itertools

# Code examples from GvR
# https://mail.python.org/pipermail/python-dev/2015-April/139054.html

# Correct ###


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None


def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

# Not correct ###
#: W701:1:1
def foo(x):
    if x >= 0:
        return math.sqrt(x)
#: W700:3:9
def bar(x):
    if x < 0:
        return
    return math.sqrt(x)

# More examples for the sake of testings

# Correct ###


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    elif x == 0:
        return 0
    else:
        return None


def goldback_conjecture():
    for i in itertools.count(2):
        if not can_be_expressed_as_prime_sum(i):
            return i
    assert False

# Not correct ###


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    elif x == 0:
        return 0


def goldback_conjecture():
    for i in itertools.count(2):
        if not can_be_expressed_as_prime_sum(i):
            return i
